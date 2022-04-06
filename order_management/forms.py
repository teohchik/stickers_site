# from django.core.exceptions import ValidationError
# from django.forms import ModelForm, TextInput
# from storage.models import StickersStorage
#
#
# class GetQuantityDimaForm(ModelForm):
#     class Meta:
#         model = StickersStorage
#         fields = ['quantity_dima']
#
#         widgets = {
#             "quantity": TextInput(attrs={
#                 'class': 'form-quantity',
#                 'placeholder': '25',
#             }),
#         }
#
#     def clean_quantity_dima(self):
#         if self.cleaned_data['quantity_dima'] == 1:
#             raise ValidationError('Кастомна валідація')
#         return self.cleaned_data['quantity_dima']
#
#
# class GetQuantityVladForm(ModelForm):
#     class Meta:
#         model = StickersStorage
#         fields = ['quantity_vlad']
#
#         widgets = {
#             "quantity": TextInput(attrs={
#                 'class': 'form-quantity',
#                 'placeholder': '25',
#             }),
#         }
