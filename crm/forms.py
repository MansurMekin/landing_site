from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
