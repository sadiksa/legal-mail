from django import forms

class RawForm(forms.Form):
    textFile = forms.CharField(widget=forms.Textarea(attrs={'cols': 80,}), label="", )


GEEKS_CHOICES =( 
    ("1", "Sözleşmeden Dönerek Para İadesi"), 
    ("2", "Satış Bedelinden İndirim"), 
    ("3", "Ücretsiz Onarım"), 
    ("4", "Misli İle Değişim"), 
    
) 
  

class AyipliForm(forms.Form):
    secimlikhak = forms.ChoiceField(choices = GEEKS_CHOICES, label="Seçimlik Hakkınızı Seçiniz", widget=forms.Select(attrs={'class': "form-control"}))
    teslimtarihi = forms.DateField(label="Teslim Alma Tarihi", input_formats=["%d/%m/%Y",], widget=forms.DateInput(attrs={'class': "form-control"}))

class Sonuc():
    tercih = ""
    teslimtarihi = ""
    zamanasimi = ""
    ispatsatici = ""
    metin = ""
    ayipGenel = """
    Ayıplı mal Tüketici Kanunu 8. madde 1. fıkrasında açıkça tanımlanmıştır. Malın tüketiciye teslimi anında,
taraflarca kararlaştırılmış olan örnek ya da modele uygunolmaması ya da objektif olarak sahip olması
gereken özellikleri taşımaması durumunda mal ayıplı mal kabul edilmiştir. Uyuşmazlık konusu mal da kanun gereğince 
ayıplı bir maldır. Tüketici Kanunu ayıplı mal durumunda tüketiciye dört adet seçimlik hak tanımıştır. İlgili madde:
'MADDE 11- (1) Malın ayıplı olduğunun anlaşılması durumunda tüketici;
a) Satılanı geri vermeye hazır olduğunu bildirerek sözleşmeden dönme,
b) Satılanı alıkoyup ayıp oranında satış bedelinden indirim isteme,
c) Aşırı bir masraf gerektirmediği takdirde, bütün masrafları satıcıya ait olmak üzere satılanın ücretsiz onarılmasını
isteme,
ç) İmkân varsa, satılanın ayıpsız bir misli ile değiştirilmesini isteme,
seçimlik haklarından birini kullanabilir. Satıcı, tüketicinin tercih ettiği bu talebi yerine getirmekle yükümlüdür.' 
    """
    a = "Tüketici Kanunu 11. maddesi (a) fıkrası gereğince satılanı geri vermeye hazır olduğumu bildiriyor ve sözleşmeden dönmek istiyorum."
    b = "Tüketici Kanunu 11. maddesi (b) fıkrası gereğince maldaki  ayıp oranında satış bedelinden indirim istiyorum."
    c = "Tüketici Kanunu 11. maddesi (c) fıkrası gereğince  bütün masrafları satıcıya ait olmak üzere satılanın ücretsiz onarılmasını istiyorum."
    d = "Tüketici Kanunu 11. maddesi (ç) fıkrası gereğince  satılanın ayıpsız bir misli ile değiştirilmesini istiyorum."
