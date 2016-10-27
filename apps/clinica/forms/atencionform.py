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

from ..models.atencion import Atencion
from ..models.vacunacion import Vacunacion, VACUNA
from ..models.colamedica import ColaMedica, ESTADOS

class AtencionForm(forms.ModelForm):
    """Tipo Documeto Form."""

    person_id = forms.CharField(widget=forms.HiddenInput(), required=False,)
    historia = forms.CharField(widget=forms.HiddenInput(), required=False,)
    class Meta:
        """Meta."""
        model = Atencion
        exclude = ()
        fields = ['anamnesis','diagnostico','dx','hallasgos_clinicos',]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)

        super(AtencionForm, self).__init__(*args, **kwargs)

        self.fields['descripcion'] = forms.CharField(
            label=capfirst(_(u'Descripcion:')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['estado'] = forms.BooleanField(
            label=capfirst(_(u'estado:')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        #form para consultas
        self.fields['anamnesis'] = forms.CharField(
            label=capfirst(_(u'Anamnesis y/o Descripcion:')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['diagnostico'] = forms.CharField(
            label=capfirst(_(u'diagnostico:')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['dx'] = forms.CharField(
            label=capfirst(_(u'dx:')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['hallasgos_clinicos'] = forms.CharField(
            label=capfirst(_(u'hallasgos_clinicos:')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['motivo_atencion'] = forms.CharField(
            label=capfirst(_(u'motivo_atencion:')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['observacion'] = forms.CharField(
            label=capfirst(_(u'observacion:')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['pronostico'] = forms.CharField(
            label=capfirst(_(u'pronostico:')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['pruebas_auxiliares'] = forms.CharField(
            label=capfirst(_(u'pruebas_auxiliares:')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['tratamiento'] = forms.CharField(
            label=capfirst(_(u'tratamiento:')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        #form para vacunacion
        self.fields['vacuna'] = forms.ChoiceField(
            label=capfirst(_(u'Vacuna')), required=False,
            choices=VACUNA,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )

        self.fields['fecha_programada'] = forms.DateTimeField(
            label=_(u'Fecha Programada'), required=False,
            initial=datetime.now().replace(tzinfo=get_current_timezone()),
            widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S',),
            input_formats=(
                '%d/%m/%Y', '%d/%m/%y', '%d-%m-%Y', '%d-%m-%y', '%Y-%m-%d',
                '%Y-%m-%d %H:%M:%S'),
            help_text=u'<small class="help-error"></small> %s' % _(
                u'Some useful help text.'),
        )
        self.fields['Observacion'] = forms.CharField(
            label=capfirst(_(u'Observacion:')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        #form notas
        self.fields['ndescripcion'] = forms.CharField(
            label=capfirst(_(u'Descripcion:')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('person_id',),
            TabHolder(
                Tab(_('Atencion'),
                    Row(
                        Div(Field('descripcion', css_class='input-required'),
                        css_class='col-md-12'),
                        Div(Field('estado', ),
                        css_class='col-md-6'),
                    ),
                    Row(
                        Div(Field('mascota', css_class='input-required'),
                        css_class='col-md-12'),
                        Div(Field('colamedica', ),
                        css_class='col-md-6'),
                        Div(Field('consulta', ),
                        css_class='col-md-6'),
                        Div(HTML('<a href="/clinica/consulta/crear/" class="btn btn-warning btn-sm text-bold" rel="tooltip" title="Agregar consulta"><i class="btn-icon-only fa fa-hospital-o"></i></a>', ),
                        css_class='col-md-6'),
                        Div(Field('notas', ),
                        css_class='col-md-6'),
                        Div(Field('vacunacion', ),
                        css_class='col-md-6'),
                    ),
                ),
                Tab(_('Consulta'),
                    Row(
                        Div(Field('anamnesis', css_class='input-required'),
                        css_class='col-md-12'),
                        Div(Field('diagnostico', ),
                        css_class='col-md-6'),
                        Div(Field('dx', ),
                        css_class='col-md-6'),
                        Div(Field('hallasgos_clinicos', ),
                        css_class='col-md-6'),
                        Div(Field('motivo_atencion', ),
                        css_class='col-md-6'),
                        Div(Field('observacion', ),
                        css_class='col-md-6'),
                        Div(Field('pronostico', ),
                        css_class='col-md-6'),
                        Div(Field('pruebas_auxiliares', ),
                        css_class='col-md-6'),
                        Div(Field('tratamiento', ),
                        css_class='col-md-6'),
                    ),
                ),
                Tab(_('Vacuna'),
                    Row(
                        Div(Field('vacuna', css_class='input-required'),
                        css_class='col-md-6'),
                        Div(Field('fecha_programada', ),
                        css_class='col-md-6'),
                        Div(Field('Observacion', ),
                        css_class='col-md-12'),
                    ),
                ),
                Tab(_('Notas'),
                    Row(
                        Div(Field('descripcion', css_class='input-required'),
                        css_class='col-md-12'),
                    ),
                ),
            ),
            Row(
                FormActions(
                    smtSave(),
                    btnCancel(),
                ),
            ),
        )
class AtencionMascotaForm(forms.ModelForm):
    """ """
    class Meta:
        model = ColaMedica
        exclude= []

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)

        super(AtencionMascotaForm, self).__init__(*args, **kwargs)

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
        self.fields['veterinario'] = forms.CharField(
            label=capfirst(_(u'veterinario')), required=True,
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
                Tab(_('Perfil'),
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

                Tab(_('Historial Clinico'),
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
                                <label class="control-label"> {{ form.veterinario.label }} </label>
                                <div class="controls ">{{ form.veterinario.value }}</div>
                                </div>
                                '''),
                            css_class='col-md-6'),
                    ),
                ),
            ),
            Row(
                FormActions(
                    smtSave(),
                    btnCancel(),
                ),
            ),
        )
