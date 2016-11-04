u"""Módulo Cita."""

from django import forms
from ..models.cita import Cita
from django.utils.translation import ugettext_lazy as _
from crispy_forms.layout import Field, Div, Row, HTML
from crispy_forms.bootstrap import FormActions, TabHolder, Tab
from crispy_forms.helper import FormHelper, Layout
from apps.utils.forms import smtSave, btnCancel, btnReset
from django.utils.text import capfirst, get_text_list


class CitaForm(forms.ModelForm):
    u"""Cita."""

    class Meta:
        """Meta."""
        model = Cita
        exclude = ('estado',)
        fields = ('descripcion', 'date',
                  'evento', 'veterinario', 'cliente')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)
        super(CitaForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['readonly'] = True
        self.fields['descripcion'] = forms.CharField(
            required=False,
            widget=forms.Textarea(attrs={'rows': 3, }),
        )
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Div(Field('cliente',), css_class='col-md-6'),
                Div(Field('veterinario', ), css_class='col-md-6'),
            ),
            Row(
                Div(Field('evento',), css_class='col-md-6'),
                Div(Field('date',), css_class='col-md-6'),
            ),
            Row(
                Div(Field('descripcion',), css_class='col-md-12'),
            ),
            Div(Row(
                FormActions(
                    smtSave(),
                    btnCancel(),
                    btnReset(),
                ),
            ), css_class='modal-footer',),
        )
