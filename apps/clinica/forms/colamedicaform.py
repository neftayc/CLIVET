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

from ..models.colamedica import ColaMedica

class ColaMedicaForm(forms.ModelForm):
    """Tipo Documeto Form."""
    class Meta:
        """Meta."""
        model = ColaMedica
        exclude = ()
        fields = ['historia','descripcion','veterinario',]


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
        self.helper.layout = Layout(
            Div(
                Div(
                    Row(
                        Div(Field('historia', css_class='input-required'),
                        css_class='col-md-12'),
                        Div(Field('descripcion', ),
                        css_class='col-md-6'),
                        Div(Field('veterinario', ),
                        css_class='col-md-6'),
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
                    css_class='modal-footer'
                    ),
                css_class='modal-lg panel  panel-info modal-dialog'
            ),
        )
