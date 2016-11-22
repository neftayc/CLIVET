from django import forms
from apps.compras.models.Proveedor import Proveedor
from apps.utils.forms import smtSave, btnCancel, btnReset
from crispy_forms.helper import FormHelper, Layout
from django.utils.translation import ugettext_lazy as _
from crispy_forms.layout import Field, Div, Row, HTML
from crispy_forms.bootstrap import FormActions, TabHolder, Tab, StrictButton, FieldWithButtons
from crispy_forms.helper import FormHelper, Layout


class ProveedorForm(forms.ModelForm):

    class Meta:
        """Meta."""

        model = Proveedor
        exclude = ()
        Field = ('tipodoc', 'numdoc', 'razon_social',
                 'representante_legal', 'direccion', 'telefono',
                 'email', 'enti_bancaria', 'num_cuenta',
                 'estado')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)
        super(ProveedorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Div(Field('razon_social', placeholder="YYYY-MM-DD"),
                    css_class='col-md-5'),
                Div(Field('tipodoc', placeholder="username"), css_class='col-md-4'),
                Div(Field('numdoc', placeholder="username"), css_class='col-md-3'),
            ),
            Row(
                Div(Field('representante_legal', placeholder="username"),
                    css_class='col-md-5'),
                Div(Field('direccion', placeholder="username"),
                    css_class='col-md-4'),
                Div(Field('telefono', placeholder="YYYY-MM-DD"),
                    css_class='col-md-3'),
            ),
            Row(
                Div(Field('email', placeholder="username"), css_class='col-md-4'),
                Div(Field('enti_bancaria', placeholder="username"),
                    css_class='col-md-4'),
                Div(Field('num_cuenta', placeholder="YYYY-MM-DD"),
                    css_class='col-md-4'),
            ),
            Row(
                Div(Field('estado', placeholder="YYYY-MM-DD"), css_class='col-md-3'),
            ),
            Div(Row(
                FormActions(
                    smtSave(),
                    btnCancel(),
                    btnReset(),
                ),
            ), css_class='modal-footer',),
        )
