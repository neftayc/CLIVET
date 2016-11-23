from django import forms
from ..models.compra import Compra
from apps.ventas.models.Producto import Producto
from apps.compras.models.Proveedor import Tipo_Documento


class CompraForm(forms.ModelForm):
    u"""Tipo Documeto Form."""
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        required=False,
        label="",
        help_text="",
        empty_label=None,
        widget=forms.Select(
            attrs={'class': 'chosen-select',
                   'data-placeholder': 'Eliga el producto'})
    )
    data_compra = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'type': 'hidden'}))

    comprobante = forms.ImageField(required=False)
    # =====================modal==========================
    tipo_doc = forms.ChoiceField(
        choices=Tipo_Documento, required=False,
        label='Tipo de documento')

    class Meta:

        model = Compra
        fields = ('total', 'proveedor',)
        exclude = ()
        widgets = {
            'proveedor': forms.Select(
                attrs={'class': 'chosen-select',
                       'data-placeholder': 'Choose a Country'}),
            'total': forms.TextInput(attrs={'class': 'form-control'}), }

    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        self.fields['proveedor'].empty_label = None
