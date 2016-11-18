#encoding: utf-8
from django import forms

from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst, get_text_list
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Div, Row, HTML
from crispy_forms.bootstrap import FormActions, TabHolder, Tab, StrictButton

from apps.utils.forms import smtSave, btnCancel, btnReset


from django.utils.timezone import get_current_timezone
from datetime import datetime

from ..models.colamedica import ColaMedica
from ..models.mascota import Mascota
from apps.clivet.models.cliente import Cliente

class ColaMedicaForm(forms.ModelForm):
    """Tipo Documeto Form."""
    cliente = forms.ModelChoiceField(
            queryset=Cliente.objects.all(), required=False, )
    mascotas = forms.ModelChoiceField(
            queryset=Mascota.objects.all(), required=False, )
    class Meta:
        """Meta."""
        model = ColaMedica
        exclude = ()
        fields = ['historia','descripcion','medico',]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)

        super(ColaMedicaForm, self).__init__(*args, **kwargs)

        self.fields['descripcion'] = forms.CharField(
            label=capfirst(_(u'Descripcion:')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Div(
                Div(
                    Row(
                        Div(
                            Field('cliente', data_placeholder="Pruebas Auxiliares", css_class="chosen-select select-medica", tabindex="6"),
                        css_class="col-xs-12 col-md-5"),
                        Div(
                            Div(
                                HTML('''<a href="/clivet/cliente/crear" class="btn btn-medica  text-bold btn-block" title="Agregar"><i class="btn-icon-onlyx fa fa-plus"></i> Agregar Cliente</a>'''),
                            css_class="col-xs-12 col-md-6"),
                            Div(
                                HTML('''<a class="btn btn-medica text-bold btn-block" href="/clinica/mascota/crear/"><i class="btn-icon-onlyx fa fa-plus"></i> Agregar Mascota</a>'''),
                            css_class="col-xs-12 col-md-6"),
                        css_class="col-md-7"),
                    ),
                    Div(HTML('''<hr>'''),),
                    Row(
                        Div(
                            Div(
                                HTML('''<table class=" panel panel-medica table table-hover">
                                    <thead class="medica-table">
                                        <tr>
                                            <th>N° Historia</th>
                                            <th>Mascota</th>
                                            <th class="btn-actions col-blocked text-center">Seleccionar</th>
                                        </tr>
                                    </thead>
                                    <tbody  id="datos">
                                    </tbody>
                                </table>'''),
                            css_class=""),
                        css_class="col-xs-5"),
                        Div(
                            Div(
                                Div(
                                    HTML('''
                                    <li class="list-group-item active  titlehistoria text-center">
                                        <span><i class="fa fa-github"></i> Elige a una mascota en la tabla</span>
                                        </li>
                                    '''),
                                    Field('mascotas',disabled="true"),
                                css_class="list-group vacuna"),
                            css_class="col-md-6"),
                            Div(
                                Div(
                                    HTML('''
                                    <li class="list-group-item active titlehistoria text-center">
                                        <span><i class="fa fa-github"></i> Elija el Doctor encargado </span>
                                        </li>
                                    '''),
                                    Field('medico'),
                                css_class="list-group vacuna"),
                            css_class="col-md-6"),
                            Div(Field('historia', css_class='input-required'),
                            css_class='col-md-12'),
                            Div(
                                Div(
                                    HTML('''
                                    <li class="list-group-item active titlehistoria text-center">
                                        <span><i class="fa fa-github"></i> Escriba una breve Descripcion </span>
                                        </li>
                                    '''),
                                    Field('descripcion', placeholder="Descripcion"),
                                css_class="list-group vacuna"),
                            css_class="col-md-12"),
                        Div(
                            FormActions(
                                Div(
                                    StrictButton('<i class="btn-icon-onlyx fa fa-save"></i> Agregar', type="submit", name="submit", css_class="btn btn-medica-add text-bold btn-block", css_id="submit-id-submit", title="Agregar"),),
                            ),
                        css_class="col-xs-12"),
                        css_class="col-xs-12 col-md-7"),
                    css_id="asignar"),
                ),
            ),
        )
