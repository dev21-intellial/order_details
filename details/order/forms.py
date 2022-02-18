from dataclasses import field, fields
from pyexpat import model
from django import forms
from django import forms 
from order.models import order1

class orderform(forms.ModelForm):
    class Meta:
        model=order1
        fields="__all__"
        Widgets={
            'customer': forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'})),
            'product':forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'})),
            'Qty':forms.IntegerField(),
            'unitprice':forms.IntegerField(),
            'totalprice':forms.IntegerField(),
        }



