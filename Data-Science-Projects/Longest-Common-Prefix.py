def longestcommonprefix():
    normal_liste = []
    sıralar_listesi = []
    kontrol_edilecek_kelimeler = input("3 tane kelime giriniz:")
    kontrol_edilecek_kelimeler1 = kontrol_edilecek_kelimeler.split()
    for i in range(len(kontrol_edilecek_kelimeler1)):
        kontrol_edilecek_harfler =list(kontrol_edilecek_kelimeler1[i])
        normal_liste += kontrol_edilecek_harfler
        sıralar = len(kontrol_edilecek_kelimeler1[i])
        sıra_listesi = list(str(sıralar))
        sıralar_listesi += sıra_listesi 
    kelime1 = normal_liste[0:int(sıralar_listesi[0])]
    kelime2 = normal_liste[int(sıralar_listesi[0]):(int(sıralar_listesi[0])+(int(sıralar_listesi[1])))]
    kelime3 = normal_liste[(int(sıralar_listesi[0])+(int(sıralar_listesi[1]))):]
    en_kısa_kelime = min(kelime1,kelime2,kelime3,key=len)
    for i in range(len(en_kısa_kelime)):
        if kelime1[i] == kelime2[i] == kelime3[i]:
            print(kelime1[i])
        else:
            print("")
   
longestcommonprefix()
