#encoding: utf-8
from django import forms

from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst, get_text_list
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Div, Row, HTML, Submit
from crispy_forms.bootstrap import FormActions, TabHolder, Tab,  PrependedText, Accordion,  AccordionGroup, StrictButton, AppendedText

from apps.utils.forms import smtSave, btnCancel, btnReset
from django.utils.timezone import get_current_timezone
from datetime import datetime

from ..models.atencion import Atencion
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
        fields = ['temperatura', 'fc', 'fr', 'kg', 'porcentaje', 'tlc', 'anamnesis', 'diagnostico', 'dx', 'hallasgos_clinicos', 'motivo_atencion', 'observacion', 'pronostico', 'pruebas_auxiliares', 'tratamiento', 'fecha_programada', 'vobservacion', 'vacuna', 'ndescripcion', ]

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
        self.fields['temperatura'] = forms.CharField(
            label=capfirst(_(u'T°')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )

        self.fields['anamnesis'] = forms.CharField(
            widget = forms.Textarea(),
            label=capfirst(_(u'Anamnesis y/o Descripcion:')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['dx'] = forms.CharField(
            label=capfirst(_(u'dx:')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )

        self.fields['motivo_atencion'] = forms.CharField(
            label=capfirst(_(u'motivo_atencion:')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['vobservacion'] = forms.CharField(
            label=capfirst(_(u'observacion:')), required=False,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.fields['pronostico'] = forms.CharField(
            label=capfirst(_(u'pronostico:')), required=True,
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
                u''),
        )
        self.fields['observacion'] = forms.CharField(
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
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field('person_id',),
            Div(
                Div(
                    HTML('''
                    <div class="row">
                    <div class="col-md-12"><h1 class="text-center detail-subtitle">Registro de Atencion</h1></div>
                        <div class="col-md-4">
                            <div class="form-group">
                                <label class="col-sm-3 control-label detail-label">Mascota:</label>
                                <div class="col-sm-9">
                                    <p class="form-control-static detail-form"> Atendiendo al paciente {{ form.nombre.value}}</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="form-group">
                                <label class="col-sm-3 control-label detail-label"> {{ form.dueño.label }}: </label>
                                <div class="col-sm-9">
                                    <p class="form-control-static detail-form"> {{ form.dueño.value }} </p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="form-group">
                                <label class="col-sm-3 control-label detail-label"> {{ form.raza.label }}: </label>
                                <div class="col-sm-9">
                                    <p class="form-control-static detail-form"> {{ form.raza.value }} </p>
                                </div>
                            </div>
                        </div>'''),
                css_class="panel-cabecera"),
            ),
            Div(
                Div(
                    Div(
                        HTML('''
                            <h4 class="panel-title">
                                <a role="button" data-toggle="collapse" data-parent="#accordion" href="#collapseOne" aria-expanded="true" aria-controls="collapseOne">Iniciar Consulta</a>
                            </h4>
                        '''),
                    css_class="panel-heading", role="tab", css_id="headingOne"),
                    Div(
                        Div(
                            Div(
                                Row(
                                    Div(
                                        Div(Field('estado', ), css_class='col-md-12'),
                                    css_class="estado-oculto"),
                                    Div(
                                        PrependedText('fecha_programada', '<i class="fa fa-calendar"></i>  Fecha', disabled='true'),
                                            css_class="col-md-4"),
                                    Div(
                                        PrependedText('motivo_atencion', 'Motivo Atencion:', placeholder="motivo atencion"),
                                    css_class="col-md-8"),
                                css_class="listado"),
                                Row(
                                    Div(PrependedText('temperatura', 'T°', placeholder="temperatura"),css_class="col-md-2"),
                                    Div(PrependedText('fc', ' FC', placeholder="fc"),css_class="col-md-2"),
                                    Div(PrependedText('fr', ' FR', placeholder="fr"),css_class="col-md-2"),
                                    Div(PrependedText('kg', ' Kg', placeholder="kilogramos"),css_class="col-md-2"),
                                    Div(PrependedText('porcentaje', ' %', placeholder="porcentaje"),css_class="col-md-2"),
                                    Div(PrependedText('tlc', ' TLC', placeholder="tlc"),css_class="col-md-2"),
                                css_class="listado"),
                                Row(
                                        Div(
                                            Div(
                                                Div(
                                                    PrependedText('anamnesis', ' Anamnesis:', placeholder="Ingrese una breve descripcion del estado actual del paciente", rows="3"),
                                                css_class="col-md-12"),
                                                Div(
                                                Div(
                                                HTML('''
                                                <li class="list-group-item active  text-center">
                                                <span><i class="fa fa-ambulance"></i> Hallasgos Clinicos</span>
                                                </li>
                                                '''),
                                                Field('hallasgos_clinicos', data_placeholder="Buscar...", css_class="chosen-select", multiple="true", tabindex="6"),
                                                css_class="list-group buscar-consulta"),
                                                css_class="col-md-6"),
                                                Div(
                                                    Div(
                                                        HTML('''
                                                            <li class="list-group-item active  text-center">
                                                                 <span><i class="fa fa-ambulance"></i> Diagnostico</span>
                                                            </li>
                                                        '''),
                                                        Field('diagnostico', data_placeholder="Buscar...", css_class="chosen-select", multiple="true", tabindex="6"),
                                                    css_class="list-group buscar-consulta"),
                                                css_class="col-md-6"),
                                                Div(
                                                PrependedText('dx', 'Trauma:', placeholder="Trauma"),
                                                css_class="col-md-6"),
                                                Div(
                                                PrependedText('pronostico', 'Pronostico:', placeholder="pronostico"),
                                                css_class="col-md-6"),
                                                Div(
                                                    Div(
                                                        HTML('''
                                                            <li class="list-group-item active  text-center">
                                                                 <span><i class="fa fa-ambulance"></i> Pruebas Auxiliares</span>
                                                            </li>
                                                        '''),
                                                        Field('pruebas_auxiliares', data_placeholder="Buscar...", css_class="chosen-select", multiple="true", tabindex="6"),
                                                    css_class="list-group buscar-consulta"),
                                                css_class="col-md-6"),
                                                Div(
                                                    Div(
                                                        HTML('''
                                                            <li class="list-group-item active  text-center">
                                                                 <span><i class="fa fa-ambulance"></i> Tratamiento</span>
                                                            </li>
                                                        '''),
                                                        Field('tratamiento', data_placeholder="Buscar...", css_class="chosen-select", multiple="true", tabindex="6"),
                                                    css_class="list-group buscar-consulta"),
                                                css_class="col-md-6"),
                                                Div(
                                                    PrependedText('observacion', 'Observacion:', placeholder="observacion"),
                                                css_class="col-md-12 hola-hola"),
                                            css_class="row list-group listado"),
                                        css_class="col-md-12"),
                                    ),
                            css_id="consultaform"),
                        css_class="panel-body"),
                    css_id="collapseOne", css_class="panel-collapse collapse", role="tabpanel", labelledby="headingOne"),
                css_class="panel pa-consulta"),
                Div(
                                Div(
                                    HTML('''
                                        <h4 class="panel-title">
                                            <a role="button" data-toggle="collapse" data-parent="#accordion" href="#collapseTwo" aria-expanded="true" aria-controls="collapseTwo">Aplicar Vacuna</a>
                                        </h4>
                                    '''),
                                css_class="panel-heading", role="tab", css_id="headingTwo"),
                                Div(
                                    Div(
                                        Div(
                                            Row(
                                                Div(
                                                    Div(
                                                        PrependedText('fecha_programada', 'F. Aplicada'),
                                                        PrependedText('vobservacion', 'Comentario', placeholder="Ingrese un comentario si hubiera"),
                                                    css_class="list-group listado"),
                                                css_class="col-md-8"),
                                                Div(
                                                    Div(
                                                        HTML('''
                                                            <li class="list-group-item active  text-center">
                                                                 <span><i class="fa fa-ambulance"></i> Vacunas Aplicadas</span>
                                                            </li>
                                                        '''),
                                                        Field('vacuna', data_placeholder="Buscar...", css_class="chosen-select", multiple="true", tabindex="6"),
                                                    css_class="list-group vacuna"),
                                                css_class="col-md-4"),
                                            ),
                                        css_id="vacunacionform"),
                                    css_class="panel-body"),
                                css_id="collapseTwo", css_class="panel-collapse collapse", role="tabpanel", labelledby="headingTwo"),
                            css_class="panel pa-vacuna panel-danger"),
                            Div(
                                Div(
                                    HTML('''
                                        <h4 class="panel-title">
                                            <a role="button" data-toggle="collapse" data-parent="#accordion" href="#collapseThree" aria-expanded="true" aria-controls="collapseThree">Agregar Nota</a>
                                        </h4>
                                    '''),
                                css_class="panel-heading", role="tab", css_id="headingThree"),
                                Div(
                                    Div(
                                        Div(
                                            Row(
                                                Div(
                                                    PrependedText('ndescripcion', '<i class="fa fa-plus"></i> Nota', placeholder="Escribir una nota "),
                                                css_class="col-md-6 listado"),
                                            ),
                                        css_id="notasform"),
                                    css_class="panel-body"),
                                css_id="collapseThree", css_class="panel-collapse collapse", role="tabpanel", labelledby="headingThree"),
                            css_class="panel pa-notas panel-success"),
                        css_class="panel-group", css_id="accordion", role="tablist", multiselectable="true"),

                        Row(
                            FormActions(
                                Div(
                                    StrictButton('<i class="btn-icon-onlyx fa fa-save"></i> Terminar Atencion', type="submit", name="submit", css_class="btn btn-info text-bold", css_id="submit-id-submit", title="Grabar"),
                                    StrictButton('<i class="btn-icon-onlyx fa fa-ban"></i> Cancelar', type="button", name="cancel", css_class="btn btn btn-danger btn-back text-bold", css_id="button-id-cancel", title="Cancel"),
                                    StrictButton('<i class="btn-icon-onlyx fa fa-undo"></i> Reset', type="reset", name="reset", css_class="btn btn btn-default text-bold", css_id="reset-id-reset", title="Reset"),
                                css_class="col-xs-12"),
                            ),
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
                            css_class='col-md-6 col-md-3 '),
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
