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
from ..models.colamedica import ColaMedica

class AtencionForm(forms.ModelForm):

    person_id = forms.CharField(widget=forms.HiddenInput(), required=False,)
    historia = forms.CharField(widget=forms.HiddenInput(), required=False,)
    nombre = forms.CharField(widget=forms.HiddenInput(), required=False,)
    raza = forms.CharField(widget=forms.HiddenInput(), required=False,)
    dueño = forms.CharField(widget=forms.HiddenInput(), required=False,)
    descripcion = forms.CharField(widget=forms.HiddenInput(), required=False,)

    class Meta:
        """Meta."""
        model = Atencion
        exclude = ()
        fields = ['anamnesis','diagnostico','dx','hallasgos_clinicos','motivo_atencion', 'observacion', 'pronostico', 'pruebas_auxiliares', 'tratamiento', 'fecha_programada', 'vobservacion', 'vacuna', 'ndescripcion',]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)

        super(AtencionForm, self).__init__(*args, **kwargs)

        self.fields['estado'] = forms.BooleanField(
            label=capfirst(_(u'Marque el check para que sea como atendido')), required=False,
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
            Row(
                Div(
                    Div(
                        Div(
                            HTML('''{% block content_title %}
                                 <div class="box-header row">
                                    <div class="a-title col-md-3"><i class="fa fa-paw"></i> Atendiendo al paciente {{ form.nombre.value}}</div>
                                    <div class="a-title col-md-2"> <strong>Especie:</strong> {{ form.raza.value}}</div>
                                    <div class="a-title col-md-4 text-center"><strong>Propietario:</strong> {{ form.dueño.value}}</div>
                                    <div class="col-md-2 col-md-offset-1 text-center"><div class="box-num">N° Historia {{ form.historia.value}}</div></div>
                                </div>
                        {% endblock content_title %}'''),
                        css_class="panel-heading"),
                        Div(
                            TabHolder(
                                Tab(_('Nueva Consulta'),
                                    Row(
                                        Div(Field('estado', ),
                                        css_class='col-md-4'),
                                        Div(Field('anamnesis', css_class='input-required'),
                                        css_class='col-md-12 has-success'),
                                        Div(Field('diagnostico', ),
                                        css_class='col-md-6 has-success'),
                                        Div(Field('dx', ),
                                        css_class='col-md-6 has-success'),
                                        Div(Field('hallasgos_clinicos', ),
                                        css_class='col-md-6 has-success'),
                                        Div(Field('motivo_atencion', ),
                                        css_class='col-md-6 has-success'),
                                        Div(Field('observacion', ),
                                        css_class='col-md-6 has-success'),
                                        Div(Field('pronostico', ),
                                        css_class='col-md-6 has-success'),
                                        Div(Field('pruebas_auxiliares', ),
                                        css_class='col-md-6 has-success'),
                                        Div(Field('tratamiento', ),
                                        css_class='col-md-6 has-success'),
                                    ),
                                ),
                                Tab(_('Agregar Vacuna'),
                                    Row(
                                        Div(Field('vacuna', css_class='input-required'),
                                        css_class='col-md-6'),
                                        Div(Field('fecha_programada', ),
                                        css_class='col-md-6'),
                                        Div(Field('Observacion', ),
                                        css_class='col-md-12'),
                                    ),
                                ),
                                Tab(_('Agregar Notas'),
                                    Row(
                                        Div(Field('vobservacion', css_class='input-required'),
                                        css_class='col-md-12'),
                                        Div(Field('ndescripcion', css_class='input-required'),
                                        css_class='col-md-12'),
                                    ),
                                ),
                            ),
                            Div(
                                FormActions(
                                    smtSave(),
                                    btnCancel(),
                                ),
                            ),
                        css_class="panel-body"),
                    css_class="panel panel-info"
                    ),
                css_class="col-md-12"),
            ),
        )
class AtencionMascotaDetailForm(forms.ModelForm):
    """ """
    class Meta:
        model = Atencion
        exclude= []

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)

        super(AtencionMascotaDetailForm, self).__init__(*args, **kwargs)

        self.fields['num_historia'] = forms.CharField(
            label=capfirst(_(u'N° Historia')), required=True,
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
                        Div(Div(HTML('''
                                <img src="/media/clivet/images.jpg"" alt="{{ form.nombre.value}}" class="img-responsive">
                                '''),
                                Div(HTML('''
                                    <h3>{{ form.nombre.value}}</h3>
                                    <p><strong>{{ form.num_historia.label }}</strong>: {{ form.num_historia.value}}</p>
                                    <button type="button" class="btn btn-info btn-lg">
                                        <i class="fa fa-calendar" aria-hidden="true"></i>
                                    </button>
                                    <button type="button" class="btn btn-warning btn-lg">
                                        <i class="fa fa-hospital-o" aria-hidden="true"></i>
                                    </button>
                                    '''
                                    ),
                                css_class='caption text-center'),
                                css_class='thumbnail'),
                            css_class='col-sm-6 col-md-3 '),
                        Div(HTML('''
                                {% include "clinica/includes/tablaperfil.html" %}
                                '''),
                            css_class='col-md-5 panel panel-default'),
                        Div(HTML('''
                                {% include "clinica/includes/tablasreport.html" %}
                                '''),
                            css_class='col-md-4'),
                    ),
                ),
                Tab(_('Historial de Compras'),
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
                Tab(_('Historia Clinico'),
                    Row(
                        Div(HTML('''
                                 {% include "clinica/includes/atencion.html" %}
                                 '''
                                 ),
                            ),
                        ),
                ),
                Tab(_('Agenda Medica'),
                ),
            ),
        )
