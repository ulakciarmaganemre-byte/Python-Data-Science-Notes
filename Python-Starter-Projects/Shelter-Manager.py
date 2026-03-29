class Hayvan:

    def __init__(self, tur, yaş, saglik, aclik):
        self.tur = tur 
        self.yaş = yaş 
        self.saglik = saglik
        self.aclik = aclik
        self.sesler = {"kedi" : "miyav" , "köpek" : "hav hav"}
    def ses_cikar(self, tur):
        if tur not in self.sesler.keys():
            return "Bu hayvanın sesi veritabanımızda yoktur!"
        else:
            return self.sesler[self.tur]
    def durum_goster(self):
        return "Sağlık Durumu: {} \nAçlık Durumu: {}".format(("+"*(self.saglik)), ("+"*(self.aclik)))

class Bakıcı(Hayvan):
    def __init__(self, isim, uzman):
        self.isim = isim
        self.uzman = uzman
    def Besle(self, hayvan, çarpan):
        if 0 < hayvan.aclik < 100:
            hayvan.aclik += çarpan
        else:
            print("hayvanın verisi gerçekçi değil!!!")
    def İyileştir(self, hayvan, çarpan):
        if 0 < hayvan.saglik < 100:
            hayvan.saglik += çarpan
        else:
            print("hayvanın verisi gerçekçi değil!!!")

class Barinak():
    def __init__(self,hyvnlr = None, bkclr = None):
        if hyvnlr is None:
            self.hyvnlr = []
        else:
            self.hyvnlr = hyvnlr
        if bkclr is None:
            self.bkclr = []
        else:
            self.bkclr = bkclr
    def gun_atlat(self):
        print("-----barınakta bir gün geçti-----")
        for hayvan in self.hyvnlr:
            hayvan.aclik += 10 
            hayvan.saglik_durumu -= 5 
    def sistemi_yukle(self):
        print("Barınaktaki Hayvanlar:")
        for hayvan in self.hyvnlr:
            print(f"- {hayvan.tur}, Yaş: {hayvan.yaş}, Sağlık: {hayvan.saglik}, Açlık: {hayvan.aclik}")
        print("\nBarınaktaki Bakıcılar:")
        for bakici in self.bkclr:
            print(f"- {bakici.isim}, Uzmanlık: {bakici.uzman}")

        
                
    
        

hayvan_1 = Hayvan("kedi", 3, 56, 56)
hayvan_2 = Hayvan("köpek", 8, 90, 67)

bakıcı_1 = Bakıcı("Osman", "Besleme")

barınak = Barinak([],[bakıcı_1])

print(hayvan_1.ses_cikar(hayvan_1.tur))
print(hayvan_1.durum_goster())
bakıcı_1.Besle(hayvan_1, 12)
bakıcı_1.İyileştir(hayvan_1, 10)
print(hayvan_1.durum_goster())
barınak.sistemi_yukle()
