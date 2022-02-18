from dataclasses import field, fields
from pyexpat import model
from django import forms
from django import forms 
from product.models import product

class productform(forms.ModelForm):
    class Meta:
        model=product
        fields="__all__"
        Widgets={
            'name':forms.TextInput(),
            'unit_price':forms.TextInput(),
            

        }



