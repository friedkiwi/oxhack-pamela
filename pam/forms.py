__author__ = 'yj'


from django import forms

from captcha.fields import ReCaptchaField

class RegisterMacForm(forms.Form):
    mac_address = forms.CharField(max_length=12, min_length=12, help_text="Please supply your MAC address in the form of aabbcc112233")
    hide_on_animation = forms.BooleanField(required=False)
    display_name = forms.CharField(max_length=42, min_length=1)
    captcha = ReCaptchaField()
