from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst, get_text_list
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Div, Row, HTML
from crispy_forms.bootstrap import FormActions, TabHolder, Tab

from unicodedata import normalize
from apps.utils.security import UserToken
from django.db.models import Q
from django.core.exceptions import NON_FIELD_ERRORS
from ..models.Venta import Venta


class VentaForm(forms.ModelForm):
    u"""Tipo Documeto Form."""

    class Meta:

        model = Venta
        fields = ('total', 'cliente', 'trabajador')
        exclude = ()
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'trabajador': forms.Select(attrs={'class': 'form-control'}),
            'total': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)

        super(VentaForm, self).__init__(*args, **kwargs)

        self.fields['username'] = forms.CharField(
            label=capfirst(_(u'username')), required=True,
            help_text=u'<small class="help-error"></small> %s' % _(
                u' '),
        )

        self.helper = FormHelper()
        self.helper.layout = Layout(

            TabHolder(
                Tab(
                    _('Account Info'),
                    Row(
                        Div(HTML('''
                                <div class="form-group">
                                <label class="control-label"> {{ form.first_name.label }} </label>
                                <div class="controls ">{{ form.first_name.value }}</div>
                                </div>
                                '''),
                            css_class='col-md-6'),
                    ),

                    Tab(_('Image'),
                        HTML("""
                        {% if form.photo.value %}<img class="img-responsive" src="{{ MEDIA_URL }}{{ form.photo.value }}">{% endif %}
                        """),
                        ),
                ),
                Row(
                    FormActions(

                      #  btnCancel(),

                    ),
                ),
            ))
