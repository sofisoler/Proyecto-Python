from django import forms

class HomeForm(forms.Form):
    name = forms.CharField(max_length=50)
    category = forms.CharField(max_length=15)
    image = forms.ImageField()