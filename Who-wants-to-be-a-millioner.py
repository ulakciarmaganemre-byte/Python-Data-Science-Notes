import random
import json

# 1. Veriyi Yükleme ve Hazırlık
try:
    with open("../data/Millioner-questions.json", "r", encoding="utf-8") as file:
        data = json.load(file)  
except FileNotFoundError:
    print("Hata: 'milyoner.json' dosyası bulunamadı!")
    exit()

sadece_metin = data["metin"]     
sadece_siklar = data["şıklar"]
sadece_cevaplar = data["cevap"]

# Global Oyun Durumu
havuz = []
joker_hakki = True


def joker_elli_elli(dogru_cevap):  # Yanlış şıklardan rastgele iki tanesini eler.
    secenekler = ["A", "B", "C", "D"]
    secenekler.remove(dogru_cevap)  # Doğruyu listeden çıkar ki elenmesin

    # Kalan 3 yanlıştan rastgele 2 tanesini seç
    elenecekler = random.sample(secenekler, 2)
    print(
        f"\n[JOKER AKTİF] Bilgi: {elenecekler[0]} ve {elenecekler[1]} şıkları yanlış, elendi!"
    )
    return elenecekler


def soru_yonetimi(baslangic_index, bitis_index, hedef_soru_sayisi):
    """Belirli bir zorluk aralığındaki soruları sorar."""
    global joker_hakki

    while len(havuz) < hedef_soru_sayisi:
        # Belirtilen aralıktan rastgele bir soru seç
        secilen_soru = random.choice(sadece_metin[baslangic_index:bitis_index])

        if secilen_soru not in havuz:
            havuz.append(secilen_soru)
            idx = sadece_metin.index(secilen_soru)
            dogru_cevap = sadece_cevaplar[idx]

            print("\n" + "=" * 30)
            print(f"SORU {len(havuz)} / 12")
            print(f"{secilen_soru}")
            print(f"{sade_sik_temizle(sadece_siklar[idx])}")  # Şıkları göster

            # Joker Kullanımı Sorusu
            if joker_hakki:
                karar = input(
                    "\n%50 Joker hakkınızı kullanmak ister misiniz? (E/H): "
                ).upper()
                if karar == "E":
                    joker_elli_elli(dogru_cevap)
                    joker_hakki = False

            # Cevap Alma
            cevap = input("\nCevabınız (A/B/C/D): ").upper()

            if cevap == dogru_cevap:
                print("✨ TEBRİKLER! Doğru cevap.")
            else:
                print(f"❌ MAALESEF YANLIŞ! Doğru cevap: {dogru_cevap}")
                return False
    return True


def sade_sik_temizle(siklar_string):
    """JSON'dan gelen şıkları daha okunaklı basar (opsiyonel)."""
    return (
        siklar_string.replace("A)", "\nA)")
        .replace("B)", "\nB)")
        .replace("C)", "\nC)")
        .replace("D)", "\nD)")
    )


def Kim_Milyoner_Olmak_Ister():
    print("***************************************")
    print("* KİM MİLYONER OLMAK İSTER'E HOŞGELDİN *")
    print("***************************************")

    # Seviye Ayarları: (Baslangic_Idx, Bitis_Idx, Hedef_Soru_Sayisi)
    seviyeler = [
        (0, 11, 4),  # Kolay Seviye (1-4. sorular)
        (10, 21, 8),  # Orta Seviye (5-8. sorular)
        (20, 30, 12),  # Zor Seviye (9-12. sorular)
    ]

    for bas, bit, hedef in seviyeler:
        if not soru_yonetimi(bas, bit, hedef):
            print("\nOyun Bitti. Toplam doğru sayınız:", len(havuz) - 1)
            return

    print("\n" + "🏆" * 15)
    print("TEBRİKLER OSMAN! 1 MİLYON TL DEĞERİNDEKİ SORUYU BİLDİN!")
    print("🏆" * 15)


# Oyunu Başlat
if __name__ == "__main__":
    Kim_Milyoner_Olmak_Ister()
