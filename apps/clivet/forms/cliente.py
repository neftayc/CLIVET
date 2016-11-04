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


class ClienteForm(forms.ModelForm):
    u"""Cliente Form."""
    nombre = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100, required=False)
    numero = forms.IntegerField(required=False)
    tipo_documento = forms.ChoiceField(choices=IDENTITY_TYPE_CHOICES)
    fecha_de_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'datepicker', }),
        required=False)
    foto_perfil = forms.ImageField(label='Selecione una foto',
                                   help_text='max. 2 megabytes',
                                   required=False)
    # apellido = forms.CharField(max_length=100,widget=forms.Textarea)
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)
    # producto = forms.ModelChoiceField(
    #     queryset=Producto.objects.all(),
    #     required=False, label="", help_text="")
    # data_venta = forms.CharField(
    #     required=False, widget=forms.TextInput(attrs={'type': 'hidden'}))
    #  hoice_field = forms.ChoiceField(widget=forms.RadioSelect,
    #                                 choices=CHOICES)

    class Meta:
        """Meta."""
        model = Cliente
        exclude = ('persona',)
        fields = ('direccion', 'ciudad', 'email', 'telefono')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Div(Field('nombre', css_class='input-required'),
                    css_class='col-md-3'),
                Div(Field('apellidos', ), css_class='col-md-4'),
                Div(Field('tipo_documento',), css_class='col-md-2'),
                Div(Field('numero',), css_class='col-md-3'),
            ),
            Row(
                Div(Field('fecha_de_nacimiento',), css_class='col-md-2'),
                Div(Field('ciudad',), css_class='col-md-2'),
                Div(Field('direccion',), css_class='col-md-3'),
                Div(Field('email',), css_class='col-md-3'),
                Div(Field('telefono',), css_class='col-md-2'),
            ),
            Row(
                Div(Field('foto_perfil',), css_class='col-md-6'),
            ),
            Div(Row(
                FormActions(
                    smtSave(),
                    btnCancel(),
                    btnReset(),
                ),
            ), css_class='modal-footer',),
        )
