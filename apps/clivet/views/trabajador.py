u"""Módulo View Cliente."""

from apps.utils.decorators import permission_resource_required
from apps.utils.forms import empty
from apps.utils.security import get_dep_objects, log_params, SecurityKey
from apps.params.models import Person
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_text
from django.utils.text import capfirst
from django.utils.translation import ugettext as _
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from ..models.cliente import Cliente
from ..forms.cliente import ClienteForm
from apps.sad.models import User
from apps.sad.forms import UserForm
from apps.params.models import Person
from django.contrib.auth.models import Permission, Group
from apps.space.models import Solution, Headquar
from apps.utils.security import SecurityKey, log_params, UserToken, get_dep_objects
from django.db import transaction
from apps.sad.models import Module, Menu, User, UserAssociation, UserEnterprise, \
    UserHeadquar, BACKEND, UserStatus, Ticket
import json
import logging
log = logging.getLogger(__name__)


class TrabajadorListView(ListView):
    u"""Tipo Documento Identidad."""

    model = User
    paginate_by = settings.PER_PAGE
    template_name = "clivet/trabajador/index.html"

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        """dispatch."""
        return super(TrabajadorListView,
                     self).dispatch(request, *args, **kwargs)

    def get_paginate_by(self, queryset):
        """Paginate."""
        if 'all' in self.request.GET:
            return None
        return ListView.get_paginate_by(self, queryset)

    def get_queryset(self):
        """Tipo Doc List Queryset."""
        self.o = empty(self.request, 'o', '-id')
        self.f = empty(self.request, 'f', '     ')
        self.q = empty(self.request, 'q', '')
        column_contains = u'%s__%s' % (self.f, 'contains')

        return self.model.objects.filter(
            **{column_contains: self.q}).order_by(self.o)

    def get_context_data(self, **kwargs):
        """
        Tipo Documento Identidad ListView List get context.

        Funcion con los primeros datos iniciales para la carga del template.
        """
        context = super(TrabajadorListView,
                        self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        # context['cmi'] = 'menu' #  Validacion de manual del menu
        context['title'] = ('Seleccione %s para editar'
                            ) % capfirst('Cliente')

        context['o'] = self.o
        context['f'] = self.f
        context['q'] = self.q.replace('/', '-')

        return context


class TrabajadorCreateView(CreateView):

    """  """
    model = User
    form_class = UserForm
    success_url = reverse_lazy('sad:user-list')

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        msg = _(u'%s is not selected or not found in the database.') % _(
            'Headquar')
        try:
            Headquar.objects.get(
                id=UserToken.get_headquar_id(self.request.session))
        except:
            messages.warning(self.request, msg)
            return HttpResponseRedirect(reverse_lazy('accounts:index'))

        key = self.kwargs.get('pk', None)
        self.person_pk = None
        if key:
            self.person_pk = SecurityKey.is_valid_key(
                self.request, key, 'user_cre')
            if not self.person_pk:
                return HttpResponseRedirect(reverse_lazy('sad:user-person_search'))

        return super(TrabajadorCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TrabajadorCreateView, self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        context['cmi'] = 'user'
        context['title'] = _('Add %s') % capfirst(_('user'))
        return context

    def get_form_kwargs(self):
        kwargs = super(TrabajadorCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_initial(self):
        initial = super(TrabajadorCreateView, self).get_initial()
        initial = initial.copy()

        if self.person_pk:
            d = Person.objects.get(pk=self.person_pk)
            if d:
                initial['photo'] = d.photo
                initial['first_name'] = d.first_name
                initial['last_name'] = d.last_name
                initial['identity_type'] = d.identity_type
                initial['identity_num'] = d.identity_num
                initial['person_id'] = d.pk
                #initial['password2'] = ''

        return initial

    @transaction.atomic
    def form_valid(self, form):
        sid = transaction.savepoint()
        try:

            t = Ticket(
                text='san',
                row=1,
                user=self.request.user
            )
            t.save()
            #raise Exception('eeee')
            try:
                person = Person.objects.get(
                    pk=self.request.POST.get("person_id"))
            except Exception as e:
                person = Person()
                person.save()
                pass
            person.first_name = form.cleaned_data['first_name']
            person.last_name = form.cleaned_data['last_name']
            person.identity_type = form.cleaned_data['identity_type']
            person.identity_num = form.cleaned_data['identity_num']
            person.photo = form.cleaned_data['photo']

            # Personalizando los mensajes de error para los Field form
            '''
            if Person.objects.exclude(id=person.id).filter(identity_type=person.identity_type, identity_num=person.identity_num).count() > 0:
                form._errors['identity_type'] = form.error_class([
                    _(u'%(model_name)s with this %(field_label)s already exists.') % {
                        'model_name': _('Person'),
                        'field_label': get_text_list((capfirst(_('Type')), capfirst(_('number'))), _('and')),
                    }
                ])
                form._errors['identity_num'] = form.error_class([
                    _(u'%(model_name)s with this %(field_label)s already exists.') % {
                        'model_name': _('Person'),
                        'field_label': get_text_list((capfirst(_('number')), capfirst(_('Type'))), _('and')),
                    }
                ])
                transaction.savepoint_rollback(sid)
                return super(TrabajadorCreateView, self).form_invalid(form)
            '''
            person.save()
            self.object = form.save(commit=False)
            self.object.person = person

            self.object.save()
            d = self.object

            headquar = Headquar.objects.get(
                id=UserToken.get_headquar_id(self.request.session))

            # agregando en UserHeadquar
            groups_sede = self.request.POST.getlist("hgroups")
            groups_sede = list(set(groups_sede))
            for value in groups_sede:
                group = Group.objects.get(id=value)
                # d.groups.add(group)
                user_profile_headquar = UserHeadquar()
                user_profile_headquar.user = d
                user_profile_headquar.headquar = headquar
                user_profile_headquar.group = group
                user_profile_headquar.save()

            # agregando en UserEnterprise
            groups_enterprise = self.request.POST.getlist("egroups")
            groups_enterprise = list(set(groups_enterprise))
            for value in groups_enterprise:
                group = Group.objects.get(id=value)
                # d.groups.add(group)
                user_profile_enterprise = UserEnterprise()
                user_profile_enterprise.user = d
                user_profile_enterprise.enterprise = headquar.enterprise
                user_profile_enterprise.group = group
                user_profile_enterprise.save()

            # agregando en UserAssociation
            groups_association = self.request.POST.getlist("agroups")
            groups_association = list(set(groups_association))
            for value in groups_association:
                group = Group.objects.get(id=value)
                # d.groups.add(group)
                user_profile_association = UserAssociation()
                user_profile_association.user = d
                user_profile_association.association = headquar.association
                user_profile_association.group = group
                user_profile_association.save()

            # agregando en user_groups
            group_dist_list = list(
                set(groups_sede + groups_enterprise + groups_association))
            for value in group_dist_list:
                group = Group.objects.get(id=value)
                d.groups.add(group)

            msg = _('The %(name)s "%(obj)s" was added successfully.') % {
                'name': capfirst(force_text(self.model._meta.verbose_name)),
                'obj': force_text(self.object)
            }
            if self.object.id:
                messages.success(self.request, msg)
                log.warning(msg, extra=log_params(self.request))
            return super(TrabajadorCreateView, self).form_valid(form)
        except Exception as e:
            try:
                transaction.savepoint_rollback(sid)
            except:
                pass
            messages.success(self.request, e)
            log.warning(force_text(e), extra=log_params(self.request))
            return super(TrabajadorCreateView, self).form_invalid(form)


class TrabajadorUpdateView(UpdateView):
    """Tipo Documento Update View."""

    model = Cliente
    form_class = ClienteForm
    template_name = "clivet/cliente/form.html"
    success_url = reverse_lazy("clivet:cliente_list")

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        """Tipo Documento Create View dispatch."""
        key = self.kwargs.get(self.pk_url_kwarg, None)
        pk = SecurityKey.is_valid_key(request, key, 'doc_upd')
        if not pk:
            return HttpResponseRedirect(self.success_url)
        self.kwargs['pk'] = pk
        try:
            self.get_object()
        except Exception as e:
            messages.error(self.request, e)
            log.warning(force_text(e), extra=log_params(self.request))
            return HttpResponseRedirect(self.success_url)

        return super(TrabajadorUpdateView,
                     self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """Tipo Documento Update View context data."""
        context = super(TrabajadorUpdateView,
                        self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        # context['cmi'] = 'empresa'
        context['title'] = ('Actualizar %s') % ('Cliente')
        return context

    def form_valid(self, form):
        """Tipo Documento Update View form_valid."""
        self.object = form.save(commit=False)
        if form.is_valid():
            if self.object.persona:
                self.object.persona.first_name = self.request.POST.get(
                    "nombre")
                self.object.persona.last_name = self.request.POST.get(
                    "apellidos")
                self.object.persona.birth_date = self.request.POST.get(
                    "fecha_de_nacimiento")
                self.object.persona.identity_num = self.request.POST.get(
                    "numero")
                self.object.persona.identity_type = self.request.POST.get(
                    "tipo_documento")
                self.object.persona.photo = self.request.POST.get(
                    "foto_perfil")
                self.object.persona.save()
                self.object.save()

        msg = ('%(name)s "%(obj)s" fue cambiado satisfacoriamente.') % {
            'name': capfirst(force_text(self.model._meta.verbose_name)),
            'obj': force_text(self.object)
        }
        if self.object.id:
            messages.success(self.request, msg)
            log.warning(msg, extra=log_params(self.request))
        return super(TrabajadorUpdateView, self).form_valid(form)

    def get_initial(self):
        context = super(TrabajadorUpdateView, self).get_initial()
        context = context.copy()
        if self.object.persona:
            context['nombre'] = self.object.persona.first_name
            context['apellidos'] = self.object.persona.last_name
            context['tipo_documento'] = self.object.persona.identity_type
            context['numero'] = self.object.persona.identity_num
            context['fecha_de_nacimiento'] = self.object.persona.birth_date and self.object.persona.birth_date.strftime(
                "%Y-%m-%d") or ""
            context['foto_perfil'] = self.object.persona.photo

        return context


class TrabajadorDeleteView(DeleteView):
    """Empresa Delete View."""

    model = Cliente
    success_url = reverse_lazy('clivet:cliente_list')

    @method_decorator(permission_resource_required)
    def dispatch(self, request, *args, **kwargs):
        """Empresa Delete View dispatch."""
        key = self.kwargs['pk']
        pk = SecurityKey.is_valid_key(request, key, 'doc_del')
        if not pk:
            return HttpResponseRedirect(self.success_url)
        self.kwargs['pk'] = pk
        try:
            self.get_object()
        except Exception as e:
            messages.error(self.request, e)
            log.warning(force_text(e), extra=log_params(self.request))
            return HttpResponseRedirect(self.success_url)
        return super(TrabajadorDeleteView,
                     self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        u"""
        Empresa Delete View delte.

        Función para eliminar la empresa sobre un metodo que verifica las
        dependencias de que tiene la tabla mostrando un mensaje de validacion.
        """
        try:
            d = self.get_object()
            deps, msg = get_dep_objects(d)
            print(deps)
            if deps:
                messages.warning(
                    self.request,
                    ('No se puede Eliminar %(name)s') %
                    {
                        "name": capfirst(force_text(
                            self.model._meta.verbose_name)
                        ) + ' "' + force_text(d) + '"'
                    })
                raise Exception(msg)

            d.delete()
            msg = _(
                ' %(name)s "%(obj)s" fuel eliminado satisfactorialmente.') % {
                'name': capfirst(force_text(self.model._meta.verbose_name)),
                'obj': force_text(d)
            }
            if not d.id:
                messages.success(self.request, msg)
                log.warning(msg, extra=log_params(self.request))
        except Exception as e:
            messages.error(request, e)
            log.warning(force_text(e), extra=log_params(self.request))
        return HttpResponseRedirect(self.success_url)

    def get(self, request, *args, **kwargs):
        """Empresa Delete View get."""
        return self.delete(request, *args, **kwargs)

    # last_headquar_id = models.CharField(max_length=50, null=True, blank=True)
    # last_module_id = models.CharField(max_length=50, null=True, blank=True)
    # person = models.OneToOneField(
    #     Person, verbose_name=_('Person'), null=True, blank=True,
    #     # unique=True OneToOneField ya es unico
    #     # related_name='user'
    # )
