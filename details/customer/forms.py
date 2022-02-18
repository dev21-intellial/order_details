from dataclasses import field, fields
from pyexpat import model
from django import forms
from django import forms 
from customer.models import customer

class customerform(forms.ModelForm):
    class Meta:
        model=customer
        fields="__all__"
        Widgets={
            'first_name':forms.TextInput(),
            'last_name':forms.TextInput(),
            'contact_no':forms.IntegerField(),
            'pincode':forms.IntegerField(),

        }



