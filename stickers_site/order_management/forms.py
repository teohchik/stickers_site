from django.forms import ModelForm, TextInput
from storage.models import StickersStorage


class GetQuantityDimaForm(ModelForm):
    class Meta:
        model = StickersStorage
        fields = ['quantity_dima']

        widgets = {
            "quantity": TextInput(attrs={
                'class': 'form-quantity',
                'placeholder': '25',
            }),
        }


class GetQuantityVladForm(ModelForm):
    class Meta:
        model = StickersStorage
        fields = ['quantity_vlad']

        widgets = {
            "quantity": TextInput(attrs={
                'class': 'form-quantity',
                'placeholder': '25',
            }),
        }