from django import forms

class ProductForm(forms.Form):
    name = forms.CharField()
    price = forms.FloatField()
    stock = forms.BooleanField(required=False)
    category = forms.CharField(max_length=15)
    description = forms.CharField()
    image = forms.ImageField()