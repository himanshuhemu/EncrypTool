from django.shortcuts import render
from myapp import forms
from myapp import form2
from myapp import enden


# Create your views here.
def index(request):
    return render(request,"index.html")
def form_(request):
    formc = forms.formClass()
    new=0
    en_txt=" " 
    e_key=" "


    if request.method=="POST":
        #new=0                              
        formc=forms.formClass(request.POST)
        if formc.is_valid():
              t=formc.cleaned_data['text']
              en_txt,e_key = enden.encryption(t)
             # print("  "+formc.cleaned_data['email']+"\n")
              #print("  "+formc.cleaned_data['text']+"\n")
    context = {"key":formc,"x":en_txt,"y":e_key}
    return render(request,"some.html",context)
def form_1(request):
    fin=' '
    forme = form2.formClass
    if request.method=="POST":
        forme=form2.formClass(request.POST)
        if forme.is_valid():
            en=forme.cleaned_data['en_text']
            enk=forme.cleaned_data['key2']
            fin=enden.dec(en,enk)
    context={"abc":forme,"t":fin}
    return render(request,"dec.html",context)
     

