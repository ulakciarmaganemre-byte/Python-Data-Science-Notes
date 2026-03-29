import datetime
import os

class EnigmaMotoru:
    def __init__(self):
        self.alfabe_alt = "abcçdefgğhıijklmnoöprsştuüvyz"
        self.alfabe_ust = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
        self.dosya_adi = "kasa.txt"

    def sifrele(self, metin, anahtar):
        sifreli_sonuc = ""
        for karakter in metin:
            if karakter in self.alfabe_alt:
                indeks = (self.alfabe_alt.find(karakter) + anahtar) % len(self.alfabe_alt)
                sifreli_sonuc += self.alfabe_alt[indeks]
            elif karakter in self.alfabe_ust:
                indeks = (self.alfabe_ust.find(karakter) + anahtar) % len(self.alfabe_ust)
                sifreli_sonuc += self.alfabe_ust[indeks]
            else:
                sifreli_sonuc += karakter # Noktalama ve boşlukları elleme
        
        # Checksum ve Tarih ekleme
        tarih = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        checksum = len(metin)
        return f"{sifreli_sonuc}|{tarih}|{checksum}"

    def coz(self, sifreli_metin, anahtar):
        # Önce veriyi parçalarına ayırıyoruz
        try:
            metin_kismi = sifreli_metin.split("|")[0]
        except IndexError:
            return "Hatalı format!"

        orijinal_metin = ""
        # Şifre çözerken anahtarı ÇIKARIYORUZ
        for karakter in metin_kismi:
            if karakter in self.alfabe_alt:
                indeks = (self.alfabe_alt.find(karakter) - anahtar) % len(self.alfabe_alt)
                orijinal_metin += self.alfabe_alt[indeks]
            elif karakter in self.alfabe_ust:
                indeks = (self.alfabe_ust.find(karakter) - anahtar) % len(self.alfabe_ust)
                orijinal_metin += self.alfabe_ust[indeks]
            else:
                orijinal_metin += karakter
        return orijinal_metin

    def dosyaya_yaz(self, veri, anahtar):
        with open(self.dosya_adi, "a", encoding="utf-8") as f:
            f.write(f"{veri}|{anahtar}\n")
        print("Sistem: Şifreli mesaj kasaya kaydedildi.")

    def analiz_et(self, metin):
        # Metin istatistikleri
        kelimeler = metin.split()
        harf_sayisi = len([c for c in metin if c.isalpha()])
        
        # En çok geçen harfi bulma (Basit bir algoritma)
        frekans = {}
        for harf in metin.lower():
            if harf.isalpha():
                frekans[harf] = frekans.get(harf, 0) + 1
        
        en_cok_gecen = max(frekans, key=frekans.get) if frekans else "Yok"
        
        print("\n--- ANALİZ RAPORU ---")
        print(f"Kelime Sayısı: {len(kelimeler)}")
        print(f"Harf Sayısı: {harf_sayisi}")
        print(f"En Çok Geçen Harf: '{en_cok_gecen}'")
        print("---------------------\n")

enigma = EnigmaMotoru()

try:
    secim = input("1- Şifrele ve Kaydet\n2- Kasadan Oku ve Çöz\nSeçiminiz: ")

    if secim == "1":
        mesaj = input("Şifrelenecek mesajı girin: ")
        key = int(input("Kaydırma anahtarı (Sayı): "))
        
        # Analiz yap
        enigma.analiz_et(mesaj)
        
        # Şifrele ve Kaydet
        sifreli = enigma.sifrele(mesaj, key)
        enigma.dosyaya_yaz(sifreli, key)
        print(f"Şifreli Format: {sifreli}")

    elif secim == "2":
        if not os.path.exists("kasa.txt"):
            print("Kasa dosyası bulunamadı!")
        else:
            with open("kasa.txt", "r", encoding="utf-8") as f:
                satirlar = f.readlines()
            
            for i, satir in enumerate(satirlar):
                print(f"{i}- {satir.split('|')[0]}...")

            secilen_idx = int(input("Hangi mesajı çözmek istersiniz? (No): "))
            girilen_anahtar = int(input("Anahtarı girin: "))
            
            # Veriyi parçala
            parcalar = satirlar[secilen_idx].strip().split("|")
            gercek_anahtar = int(parcalar[3])

            if girilen_anahtar == gercek_anahtar:
                cozulmus = enigma.coz(satirlar[secilen_idx], girilen_anahtar)
                print(f"\nMesaj Çözüldü: {cozulmus}")
            else:
                print("\n!!! ERİŞİM ENGELLENDİ: Yanlış Anahtar !!!")

except ValueError:
    print("Hata: Lütfen sayısal verileri doğru girin!")
except Exception as e:
    print(f"Beklenmedik bir hata oluştu: {e}")
