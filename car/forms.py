from django.forms import ModelForm
from django

class CarForm(ModelForm):
    class Meta:
        model=Car
        fields='__all__'

    def clean_number(self):
        number = self.cleaned_data['number']
        if '000'




# from django import forms
# from django.core.exceptions import ValidationError

# class ContactForm(forms.Form):
#     # Everything as before.
#     ...

#     def clean_recipients(self):
#         data = self.cleaned_data['recipients']
#         if "fred@example.com" not in data:
#             raise ValidationError("You have forgotten about Fred!")

