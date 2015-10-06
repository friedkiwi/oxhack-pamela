__author__ = 'yj'


from django import forms

from captcha.fields import ReCaptchaField
from .models import Device



class RegisterMacForm(forms.Form):
    mac_address = forms.ModelChoiceField(queryset=Device.objects.filter(currently_in_space=True))
    hide_on_animation = forms.BooleanField(required=False)
    display_name = forms.CharField(max_length=42, min_length=1)
    captcha = ReCaptchaField()
