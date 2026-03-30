import random

def tahmin_doğruysa():
    for i in range(len(harfler)):
      if tahmin == harfler[i]:
        gösterlist[i] = tahmin
    print(" ".join(gösterlist))

tahmin_sayısı = 0
kelimeler_listesi = ["osman","armağan","python","programlama","yapayzeka","geliştirme","yazılım","donanım","veritabanı","internet","bilgisayar","teknoloji","mühendislik","tasarım","görsel","işlemci","bellek","sistem","ağ","güvenlik" ,"uygulama"]   
seçilen_kelime = random.choice(kelimeler_listesi)
harfler = list(seçilen_kelime)        
gizli_kelime = "_" * len(seçilen_kelime)
alfabe = "abcçdefgğhıijklmnoöpqrsştuüvyz"
alfabe_listesi = list(alfabe)
gösterlist = ["_"] * len(seçilen_kelime)
print(gizli_kelime)

cevaplar = []

while not set(harfler).issubset(set(cevaplar)) and not tahmin_sayısı == 7:
    tahmin = input("lütfen bir harf tahmin ediniz. ")
    cevaplar += tahmin 
    if  0 < len(tahmin) < 2:
        tahmin_doğruysa()
        tahmin_sayısı += 1
        print(f"{tahmin_sayısı} tahmin yaptınız")
        print(f"{7-tahmin_sayısı} hakkınız kaldı.")
    else:
        print("Hata! Lütfen 1 harf giriniz.")
