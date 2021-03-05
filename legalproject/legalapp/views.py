from django.shortcuts import render, redirect
from .demo.main import demoAi
import datetime


# Create your views here.
from .forms import RawForm, AyipliForm, Sonuc

def formView(request):
    form = RawForm()
    if request.method == "POST":
        form = RawForm(request.POST)
        
        if form.is_valid():
            inputData = form.cleaned_data
            print(demoAi(inputData["textFile"]))
            Sonuc.metin = inputData["textFile"]
            controlList = demoAi(inputData["textFile"])
            if controlList[0] > controlList[1]:
                return redirect("/ayiplimal")
            elif controlList[0] < controlList[1]:
                return redirect("/abone")
            else:
                return redirect("/")
        else:
            print(form.errors)
        
    context = {
        "form" : form
    }
    return render(request, "templates/basic.html", context)

def ayipView(request):
    form2 = AyipliForm()
    if request.method == "POST":
        form2 = AyipliForm(request.POST)
        
        if form2.is_valid():
            inputData = form2.cleaned_data
            print(inputData)
            secim = inputData['secimlikhak']
            ttarihi = inputData['teslimtarihi']
            Sonuc.tercih = secim
            Sonuc.teslimtarihi = ttarihi
            print(ttarihi)
            return redirect("/sonuc")
            
            
        else:
            
            print(form2.errors)
            print(form2)
    context = {
        "form" : form2
    }
    return render(request, "templates/ayipli.html", context)

def aboneView(request):
    context = {
        "uyusmazlik" : "Abonelik Sözleşmesi"
    }
    return render(request, "templates/abone.html", context)

def sonucView(request):
    today = datetime.datetime.today()
    t = Sonuc.teslimtarihi-datetime.date(today.year, today.month, today.day)
    if t.days<183:
        Sonuc.ispatsatici = True
        Sonuc.zamanasimi = True
    elif t.days>182 and t.days<771:
        Sonuc.ispatsatici = False
        Sonuc.zamanasimi = True
    else:
        Sonuc.ispatsatici = False
        Sonuc.zamanasimi = False
    if Sonuc.ispatsatici == True:
        Sonuc.ispatsatici = "Tüketici Kanunu 10. maddeye göre teslim tarihinden itibaren ilk 6 ayda ortaya çıkan ayıplar teslim tarihinde olduğu kabul edilir. Ayıplı malın teslim alınmasının üzerinden 6 ay geçmemiştir. Sonuç olarak malın teslim tarihinde ayıplı olmadığının ispatı satıcıya aittir."
    else:
        Sonuc.ispatsatici = "İspat yükü Kullanıcıdadır.(Bu kısım aleyhinizedir.)"
    if Sonuc.zamanasimi == True:
        Sonuc.zamanasimi = "Kanunun ilgili 12. maddesine göre kanunlarda veya taraflar arasındaki sözleşmede daha uzun bir süre belirlenmediği takdirde, ayıplı maldan sorumluluk, malın tüketiciye teslim tarihinden itibaren iki yıllık zamanaşımına tabiidir. Uyuşmazlıkta zamanaşımı süresi aşılmamıştır."
    else:
        Sonuc.zamanasimi = "Zamanaşımı süresi geçmiştir.(Bu kısım aleyhinizedir.)"
    if Sonuc.tercih == "1":
        print(Sonuc.a)
        sonucL = Sonuc.a
    elif Sonuc.tercih == "2":
        print(Sonuc.b)
        sonucL = Sonuc.b
    elif Sonuc.tercih == "3":
        print(Sonuc.c)
        sonucL = Sonuc.c
    elif Sonuc.tercih == "4":
        print(Sonuc.d)
        sonucL = Sonuc.d
    else:
        pass
    context = {
        "secimlikhak" : sonucL,
        "teslim" : Sonuc.teslimtarihi,
        "ispat" : Sonuc.ispatsatici,
        "zamanasimi" : Sonuc.zamanasimi,
        "metin" : Sonuc.metin,
        "ayipGenel" : Sonuc.ayipGenel,
    }
    return render(request, "templates/sonuc.html", context)