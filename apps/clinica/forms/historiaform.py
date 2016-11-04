#encoding: utf-8
from django import forms

from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst, get_text_list
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Div, Row, HTML
from crispy_forms.bootstrap import FormActions, TabHolder, Tab


from apps.utils.forms import smtSave, btnCancel, btnReset


from django.utils.timezone import get_current_timezone
from datetime import datetime

from ..models.historia import Historial
from ..models.mascota import Mascota, BOOL_GENERO, TIPO_MASCOTA, CONDICION, Cliente

class HistoriaForm(forms.ModelForm):
    """Tipo Documeto Form."""
    class Meta:
        """Meta."""
        model = Historial
        exclude = ()
        fields = ['num_historia','usuario','mascota',]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)

        super(HistoriaForm, self).__init__(*args, **kwargs)

        self.fields['num_historia'] = forms.CharField(
            label=capfirst(_(u'N° Historia:')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(
                    Row(
                        Div(Field('num_historia', css_class='input-required'),
                        css_class='col-md-4'),
                        Div(Field('usuario', ),
                        css_class='col-md-4'),

                        Div(Field('mascota',),
                        css_class='col-md-4'),
                        ),
                    css_class='modal-body'
                    ),
                Div(
                    Row(
                        FormActions(
                            smtSave(),
                            btnCancel(),
                            btnReset(),
                            ),
                        ),
                    css_class='modal-footer '
                    ),
                css_class='modal-lg modal-dialog'
            ),
        )

class HistoriaMascotaForm(forms.ModelForm):

    """ """
    person_id = forms.CharField(widget=forms.HiddenInput(), required=False,)
    dueño = forms.CharField(widget=forms.HiddenInput(), required=False,)
    class Meta:
        model = Historial
        fields = ['num_historia','mascota','usuario',]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)

        super(HistoriaMascotaForm, self).__init__(*args, **kwargs)
        self.fields['nombre'] = forms.CharField(
            label=capfirst(_(u'nombre')),
            required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
            u' '),
        )
        self.fields['fecha_nacimiento'] = forms.DateTimeField(
            label=_(u'Fecha Nacimiento'), required=False,
            initial=datetime.now().replace(tzinfo=get_current_timezone()),
            widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S',),
            input_formats=(
                '%d/%m/%Y', '%d/%m/%y', '%d-%m-%Y', '%d-%m-%y', '%Y-%m-%d',
                '%Y-%m-%d %H:%M:%S'),
            help_text=u'<small class="help-error"></small> %s' % _(
                u'Some useful help text.'),
        )
        self.fields['genero'] = forms.ChoiceField(
            label=capfirst(_(u'genero*:')), required=False,
            choices=BOOL_GENERO,
            widget=forms.RadioSelect(attrs={'default':'macho',}),
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['especie'] = forms.ChoiceField(
            label=capfirst(_(u'tipo Mascota')), required=False,
            choices=TIPO_MASCOTA,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['raza'] = forms.CharField(
            label=capfirst(_(u'raza')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['color'] = forms.CharField(
            label=capfirst(_(u'color')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['cond_corporal'] = forms.ChoiceField(
            label=capfirst(_(u'C. Corporal')), required=False,
            choices=CONDICION,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['esterelizado'] = forms.BooleanField(
            label=capfirst(_(u'¿Esterelizado?')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['is_active'] = forms.BooleanField(
            label=capfirst(_(u'activo')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['historia'] = forms.BooleanField(
            label=capfirst(_(u'historia')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['is_actived'] = forms.BooleanField(
            label=capfirst(_(u'inactivo')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['descripcion'] = forms.CharField(
            label=capfirst(_(u'Descripcion')), required=False,
            widget=forms.Textarea(attrs = {'rows': 4, }),
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.helper = FormHelper()
        self. helper.layout = Layout(
            Field('person_id',),
            TabHolder(
                Tab(_('Mascota Info'),
                    Row(
                        Div(Field('nombre', css_class='input-required'),
                    css_class='col-md-4'),
                        Div(Field('fecha_nacimiento', css_class='input-datex'),
                    css_class='col-md-4'),
                    ),
                    Row(
                        Div(Field('especie',),
                    css_class='col-md-3'),
                        Div(Field('raza', css_class='input-required' ),
                    css_class='col-md-3'),
                        Div(Field('color', css_class='input-required'),
                    css_class='col-md-3'),
                        Div(Field('cond_corporal', ),
                    css_class='col-md-3'),
                    ),
                    Row(
                        Div(Field('genero', ),
                    css_class='col-md-4'),
                        Div(Field('esterelizado',),
                    css_class='col-md-2'),
                        Div(Field('is_active', ),
                    css_class='col-md-2'),
                        Div(Field('is_actived',),
                    css_class='col-md-2'),
                        Div(Field('historia',),
                    css_class='col-md-2'),
                    ),
                    Row(
                        Div(Field('descripcion', ),
                    css_class='col-md-12'),
                    ),
                    ),
                Tab(_('Account Info'),
                    Div(Field('num_historia', css_class='input-required'),
                    css_class='col-md-4'),
                    Div(Field('usuario', ),
                    css_class='col-md-4'),

                    Div(Field('mascota',),
                    css_class='col-md-4'),
                    ),
            ),
            Row(
                FormActions(
                    smtSave(),
                    btnCancel(),
                    btnReset(),
                ),
            ),
        )



class MascotaHistoriDetailForm(forms.ModelForm):

    """ """
    class Meta:
        model = Historial
        fields = []

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)

        super(MascotaHistoriDetailForm, self).__init__(*args, **kwargs)

        self.fields['num_historia'] = forms.CharField(
            label=capfirst(_(u'num_historia')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['created_ath'] = forms.CharField(
            label=capfirst(_(u'created_ath')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['usuario'] = forms.CharField(
            label=capfirst(_(u'usuario')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['nombre'] = forms.CharField(
            label=capfirst(_(u'nombre')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['dueño'] = forms.ChoiceField(
            label=capfirst(_(u'dueño')), required=True,
            # widget=forms.RadioSelect(),

            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['direccion'] = forms.CharField(
            label=capfirst(_(u'direccion')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['direccion'] = forms.CharField(
            label=capfirst(_(u'direccion')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['direccion'] = forms.CharField(
            label=capfirst(_(u'direccion')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['ciudad'] = forms.CharField(
            label=capfirst(_(u'ciudad')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['telefono'] = forms.CharField(
            label=capfirst(_(u'telefono')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['edad'] = forms.CharField(
            label=capfirst(_(u'edad')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['genero'] = forms.CharField(
            label=capfirst(_(u'genero')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['especie'] = forms.CharField(
            label=capfirst(_(u'especie')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['raza'] = forms.CharField(
            label=capfirst(_(u'raza')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['color'] = forms.CharField(
            label=capfirst(_(u'color')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.helper = FormHelper()
        self.helper.layout = Layout(
            TabHolder(
                Tab(
                    _('Informacion del Dueño'),
                    Row(
                        Div(HTML('''
                                <div class="form-group">
                                <label class="control-label"> {{ form.dueño.label }} </label>
                                <div class="controls ">{{ form.dueño.value }}</div>
                                </div>
                                '''),
                            css_class='col-md-6'),
                        Div(HTML('''
                                <div class="form-group">
                                <label class="control-label"> {{ form.direccion.label }} </label>
                                <div class="controls ">{{ form.direccion.value }}</div>
                                </div>
                                '''),
                            css_class='col-md-6'),
                    ),
                    Row(
                        Div(HTML('''
                                <div class="form-group">
                                <label class="control-label"> {{ form.ciudad.label }} </label>
                                <div class="controls ">{{ form.ciudad.value }}</div>
                                </div>
                                '''),
                            css_class='col-md-6'),
                        Div(HTML('''
                                <div class="form-group">
                                <label class="control-label"> {{ form.telefono.label }} </label>
                                <div class="controls ">{{ form.telefono.value }}</div>
                                </div>
                                '''),
                            css_class='col-md-6'),
                    ),

                ),
                Tab(
                    _('Informacion Mascota'),
                    Row(
                        Div(HTML('''
                                <div class="form-group">
                                <label class="control-label"> {{ form.nombre.label }} </label>
                                <div class="controls ">{{ form.nombre.value }}</div>
                                </div>
                                '''),
                            css_class='col-md-6'),
                        Div(HTML('''
                                <div class="form-group">
                                <label class="control-label"> {{ form.edad.label }} </label>
                                <div class="controls ">{{ form.edad.value }}</div>
                                </div>
                                '''),
                            css_class='col-md-6'),
                    ),
                    Row(
                        Div(HTML('''
                                <div class="form-group">
                                <label class="control-label"> {{ form.genero.label }} </label>
                                <div class="controls ">{{ form.genero.value }}</div>
                                </div>
                                '''),
                            css_class='col-md-6'),
                        Div(HTML('''
                                <div class="form-group">
                                <label class="control-label"> {{ form.especie.label }} </label>
                                <div class="controls ">{{ form.especie.value }}</div>
                                </div>
                                '''),
                            css_class='col-md-6'),
                    ),
                    Row(
                        Div(HTML('''
                                <div class="form-group">
                                <label class="control-label"> {{ form.raza.label }} </label>
                                <div class="controls ">{{ form.raza.value }}</div>
                                </div>
                                '''),
                            css_class='col-md-6'),
                        Div(HTML('''
                                <div class="form-group">
                                <label class="control-label"> {{ form.color.label }} </label>
                                <div class="controls ">{{ form.color.value }}</div>
                                </div>
                                '''),
                            css_class='col-md-6'),
                    ),
                ),

                Tab(_('Historial'),
                    Row(
                        Div(HTML('''
                                <div class="form-group">
                                <label class="control-label"> {{ form.num_historia.label }} </label>
                                <div class="controls ">{{ form.num_historia.value }}</div>
                                </div>
                                '''),
                            css_class='col-md-6'),
                        Div(HTML('''
                                <div class="form-group">
                                <label class="control-label"> {{ form.created_ath.label }} </label>
                                <div class="controls ">{{ form.created_ath.value }}</div>
                                </div>
                                '''),
                            css_class='col-md-6'),
                    ),
                    Row(
                        Div(HTML('''
                                <div class="form-group">
                                <label class="control-label"> {{ form.usuario.label }} </label>
                                <div class="controls ">{{ form.usuario.value }}</div>
                                </div>
                                '''),
                            css_class='col-md-6'),
                    ),
                ),
            ),
            Row(
                FormActions(
                    btnCancel(),
                ),
            ),
        )