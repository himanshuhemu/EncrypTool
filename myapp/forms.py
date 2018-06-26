from django import forms

class  formClass(forms.Form):
    text = forms.CharField()
    email = forms.EmailField()
    
    
