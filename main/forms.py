from django import forms
from django.conf import settings
from .models import Product,ProductColor,ProductSize,ProductSizeColor



class ProductForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    color = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',},))
    
    small=forms.BooleanField(initial=False,required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    medium=forms.BooleanField(initial=True,required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    large=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    extralarge=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))

    class Meta:
        model = ProductSizeColor
        fields = '__all__'

class ProductUpdateForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    color = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',},))
    
    small=forms.BooleanField(initial=False,required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    medium=forms.BooleanField(initial=True,required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    large=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    extra_large=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))

    class Meta:
        model = ProductSizeColor
        fields = '__all__'