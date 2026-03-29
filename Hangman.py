import random

tahmin_sayisi = 0


def tahmin_doğruysa(tahmin, harfler, gösterlist):
    global tahmin_sayisi
    if tahmin in harfler:
        for i in range(len(harfler)):
            if tahmin == harfler[i]:
                gösterlist[i] = tahmin
    else:
        tahmin_sayisi += 1

    print("Mevcut durum: " + " ".join(gösterlist))


kelimeler_listesi = ["yazılım", "python", "bilgisayar", "kodlama"]
seçilen_kelime = random.choice(kelimeler_listesi)
harfler = list(seçilen_kelime)

gösterlist = ["_"] * len(seçilen_kelime)

print(f"Kelime {len(seçilen_kelime)} harfli: " + "_ " * len(seçilen_kelime))

cevaplar = []

while not set(harfler).issubset(set(cevaplar)) and tahmin_sayisi < 7:
    tahmin = input("\nLütfen bir harf tahmin ediniz: ").lower()

    if tahmin in cevaplar:
        print("Bu harfi zaten tahmin ettiniz.")
        continue

    if len(tahmin) == 1 and tahmin.isalpha():
        cevaplar.append(tahmin)
        tahmin_doğruysa(tahmin, harfler, gösterlist)

        kalan_harf = len(set(harfler) - set(cevaplar))
        print(f"Kalan benzersiz harf sayısı: {kalan_harf}")
        print(f"{7 - tahmin_sayisi} yanlış hakkınız kaldı.")
    else:
        print("Lütfen sadece tek bir harf giriniz.")

if set(harfler).issubset(set(cevaplar)):
    print(f"\nTeberikler! Kelime: {seçilen_kelime}")
else:
    print(f"\nHakkınız bitti. Kelime şuydu: {seçilen_kelime}")
