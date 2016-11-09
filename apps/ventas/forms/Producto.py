from django import forms
from ..models.Producto import Producto
from django.utils.translation import ugettext_lazy as _
from crispy_forms.layout import Field, Div, Row, HTML
from crispy_forms.bootstrap import FormActions, TabHolder, Tab, StrictButton,FieldWithButtons
from crispy_forms.helper import FormHelper, Layout
from apps.utils.forms import smtSave, btnCancel, btnReset 	 		
from django.utils.text import capfirst, get_text_list


class ProductoForm(forms.ModelForm):
    u"""Tipo Documeto Form."""
    precioV = forms.DecimalField(widget=forms.TextInput(attrs={'type': 'number', 'class': 'form-control text-right'}))
    precioC = forms.DecimalField(widget=forms.TextInput(attrs={'type': 'number', 'class': 'form-control text-right'}))
    igv = forms.DecimalField(initial=0.00,widget=forms.TextInput(attrs={'class': 'form-control text-right'}))
    MontoReal = forms.DecimalField(initial=0.00,widget=forms.TextInput(attrs={'class': 'form-control text-right'}))
    # nombre = forms.CharField(max_length=100)
    # apellidos = forms.CharField(max_length=100, required=False)
    # numero = forms.IntegerField(required=False)
    # tipo_documento = forms.ChoiceField(choices=IDENTITY_TYPE_CHOICES)
    # fecha_de_nacimiento = forms.DateField(
    #     widget=forms.DateInput(attrs={'class': 'datepicker', }),
    #     required=False)
    # foto_perfil = forms.ImageField(label='Selecione una foto',
    #                                help_text='max. 2 megabytes',
    #                                required=False)
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
        model = Producto
        exclude = ('existencia',)
        fields = ('nombre', 'codigo', 'categoria', 'fechaVencimiento', 'unidadMedidaV',
                  'unidadMedidaC')
    #         nombre = models.CharField('Nombre', max_length=50, unique=True)
    # codigo = models.CharField('Código', max_length=50, unique=True)
    # categoria = models.ForeignKey('Categoria', Categoria)
    # fechaVencimiento = models.DateField('Fecha de Vencimiento')
    # unidadMedidaV = models.ForeignKey(
    #     UnidadMedida, related_name='ventas', verbose_name="Unidad de medida de Ventas")
    # unidadMedidaC = models.ForeignKey(UnidadMedida, related_name='compras',
    #                                   verbose_name='Unidad de medida de Compras')
    # precioV = models.DecimalField(
    #     'Precio de venta', max_digits=10, decimal_places=2)
    # precioC = models.DecimalField(
    #     'Precio de Compra', max_digits=10, decimal_places=2)
    # existencia = models.IntegerField('Cantidad de Productos')
    # MontoReal = models.DecimalField(
    #     'Monto Real', max_digits=10, decimal_places=2)
    # igv = models.DecimalField('IGV', max_digits=10, decimal_places=2)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Div(Field('nombre',placeholder="username"), css_class='col-md-6'),
                Div(Field('codigo', placeholder="username"), css_class='col-md-3'),
                Div(Field('fechaVencimiento',placeholder="YYYY-MM-DD"), css_class='col-md-3'),
            ),
            Row(
            	Div(FieldWithButtons('categoria', StrictButton("Agregar",id='addCategoria')), css_class='col-md-4'),
                Div(Field('unidadMedidaV'), css_class='col-md-4'),
                Div(FieldWithButtons('unidadMedidaC', StrictButton("Agregar", id='addUnidad')), css_class='col-md-4'),
            ),
            Div(Row(
                FormActions(
                    smtSave(),
                    btnCancel(),
                    btnReset(),
                ),
            ), css_class='modal-footer',),
        )
