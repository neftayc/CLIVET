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

from ..models.consulta import Consulta

class ConsultaForm(forms.ModelForm):
    """Tipo Documeto Form."""
    class Meta:
        """Meta."""
        model = Consulta
        exclude = ()
        fields = ['mascota','anamnesis','diagnostico','dx','hallasgos_clinicos','motivo_atencion','observacion','pronostico','pruebas_auxiliares','tratamiento',]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)

        super(ConsultaForm, self).__init__(*args, **kwargs)

        self.fields['anamnesis'] = forms.CharField(
            label=capfirst(_(u'Descripcion:')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )

        self.helper = FormHelper()
        self.helper.layout = Layout(
            TabHolder(
                    Tab(_('Perfil'),
                        Row(
                            Div(Field('mascota', css_class='input-required'),
                            css_class='col-md-12'),
                            Div(Field('anamnesis', ),
                            css_class='col-md-6'),
                            Div(Field('diagnostico', ),
                            css_class='col-md-6'),
                            Div(Field('dx', ),
                            css_class='col-md-6'),
                            ),
                        ),
                    Tab(_('Historial Clinico'),
                            Div(Field('hallasgos_clinicos', ),
                            css_class='col-md-6'),
                            Div(Field('motivo_atencion', ),
                            css_class='col-md-6'),
                            Div(Field('observacion',),
                            css_class='col-md-6'),
                            Div(Field('pronostico',),
                            css_class='col-md-6'),
                            Div(Field('pruebas_auxiliares',),
                            css_class='col-md-6'),
                            Div(Field('tratamiento',),
                            css_class='col-md-6'),
                        ),
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
        )
