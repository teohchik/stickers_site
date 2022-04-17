from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, ChoiceField, Select

from order_management.models import Order


class EditOrder(ModelForm):
    class Meta:
        model = Order
        fields = ['status']

        widgets = {
            'status': Select(attrs={
                'class': 'status'
            }),
        }

    # def clean_quantity_dima(self):
    #     if self.cleaned_data['quantity_dima'] == 1:
    #         raise ValidationError('Кастомна валідація')
    #     return self.cleaned_data['quantity_dima']


