from django import forms
from ..models.compra import Compra
from apps.ventas.models.Producto import Producto
from apps.compras.models.Proveedor import Tipo_Documento


class CompraForm(forms.ModelForm):
    u"""Tipo Documeto Form."""
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        required=False, label="", help_text="")
    data_compra = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'type': 'hidden'}))

    comprobante = forms.ImageField(help_text='max. 2 megabytes',
                                   required=False)
    # =====================modal==========================
    tipo_doc = forms.ChoiceField(
        choices=Tipo_Documento, required=False,
        label='Tipo de documento')

    class Meta:

        model = Compra
        fields = ('total', 'proveedor',)
        exclude = ()
        widgets = {
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'total': forms.TextInput(attrs={'class': 'form-control'}), }
