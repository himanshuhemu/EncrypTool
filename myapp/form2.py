from django import forms

class  formClass(forms.Form):
    Encrypted_Text = forms.CharField()
    The_key =  forms.CharField()
    