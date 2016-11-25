u"""Módulo Cliente Form."""

from django import forms
from ..models.cliente import Cliente
from apps.params.models import IDENTITY_TYPE_CHOICES
from django.utils.translation import ugettext_lazy as _
from crispy_forms.layout import Field, Div, Row, HTML
from crispy_forms.bootstrap import FormActions, TabHolder, Tab
from crispy_forms.helper import FormHelper, Layout
from apps.utils.forms import smtSave, btnCancel, btnReset
from django.utils.text import capfirst, get_text_list


class TrabajadorForm(forms.ModelForm):
    u"""Cliente Form."""
    class Meta:
        """Meta."""
        model = Cliente
        exclude = ('persona',)
        fields = ('direccion', 'ciudad', 'email', 'telefono')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)
        super(TrabajadorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Row(
                Div(Field('nombre',  placeholder='Ingrese un nombre',
                          css_class='input-required'),
                    css_class='col-md-3'),
                Div(Field('apellidos', placeholder='Ingrese sus apellidos'),
                    css_class='col-md-4'),
                Div(Field('tipo_documento',), css_class='col-md-2'),
                Div(Field('numero', placeholder='Ingrese un número'),
                    css_class='col-md-3'),
            ),
            Row(
                Div(Field('fecha_de_nacimiento', placeholder='YYYY-MM-DD'),
                    css_class='col-md-2'),
                Div(Field('ciudad', placeholder='Ingrese el nombre'),
                    css_class='col-md-2'),
                Div(Field('direccion', placeholder='Ingrese una dirección'),
                    css_class='col-md-3'),
                Div(Field('email', placeholder='example@gmail.com'),
                    css_class='col-md-3'),
                Div(Field('telefono', placeholder='Ingrese el número'),
                    css_class='col-md-2'),
            ),
            Div(Row(
                FormActions(
                    smtSave(),
                    btnCancel(),
                    btnReset(),
                ),
            ), css_class='modal-footer',),
        )
