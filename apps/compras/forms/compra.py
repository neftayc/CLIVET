from django import forms
from ..models.compra import Compra
from apps.ventas.models.Producto import Producto


class CompraForm(forms.ModelForm):
    u"""Tipo Documeto Form."""
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        required=False, label="", help_text="")
    data_compra = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:

        model = Compra
        fields = ('total', 'proveedor',)
        exclude = ()
        widgets = {
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'total': forms.TextInput(attrs={'class': 'form-control'}),
        }
