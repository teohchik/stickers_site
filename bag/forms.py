from django import forms


class EditProductInBag(forms.Form):
    quantity = forms.IntegerField(min_value=0)
    ttn = forms.CharField(max_length=30)
    price = forms.IntegerField(min_value=0)