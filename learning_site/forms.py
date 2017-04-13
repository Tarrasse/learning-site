from django import forms
from django.core import validators


def must_be_empty(value):
    if value:
        raise forms.ValidationError('its not empty')


class SuggesstionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(help_text="please verify your email address")
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label='leave empty',
                               validators=[must_be_empty])
    def clean(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data.get('email')
        verification = cleaned_data.get('verify_email')
        if email is not verification:
            raise forms.ValidationError("email don't match")


    # validators=[validators.MaxLengthValidator(0)]


    # def clean_honeypot(self):
    #     honeypot = self.cleaned_data['honeypot']
    #     if len(honeypot):
    #         raise forms.ValidationError("honeypot should be empty ")
    #     return honeypot
