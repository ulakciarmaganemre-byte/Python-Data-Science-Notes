def Döviz_dönüştürücü() :
    Türk_lirası = 1 
    Dolar = 42.70
    Euro = 50.12
    Sterlin = 57.16
    print(f"Güncel kurlar : \n Türk lirası : {Türk_lirası} \n Dolar : {Dolar} \n Euro : {Euro} \n Sterlin : {Sterlin}")
    while True :
        print("Dövizler:\n 1. Türk lirası \n 2. Dolar \n 3. Euro \n 4. Sterlin")
        dönüştürülecek_döviz = input("Lütfen dönüştürmek istediğiniz dövizin numarasını giriniz:")
        if dönüştürülecek_döviz == "1" :
            dönüştürülecek_döviz = "Türk lirası"
        elif dönüştürülecek_döviz == "2" :
            dönüştürülecek_döviz = "Dolar"
        elif dönüştürülecek_döviz == "3" :
            dönüştürülecek_döviz = "Euro"
        elif dönüştürülecek_döviz == "4" :
            dönüştürülecek_döviz = "Sterlin"
        else :
            print("Lütfen geçerli bir döviz numarası seçin")
            continue
        break
    while True :
        print("Dövizler:\n 1. Türk lirası \n 2. Dolar \n 3. Euro \n 4. Sterlin")
        dönüştürülmesi_istenen_döviz = input(f"Lütfen {dönüştürülecek_döviz}'i hangi dövize dönüştürmek istiyorsanız onun numarasını girin:" )
        if dönüştürülmesi_istenen_döviz == "1" :
            dönüştürülmesi_istenen_döviz = "Türk lirası"
        elif dönüştürülmesi_istenen_döviz == "2" :
            dönüştürülmesi_istenen_döviz = "Dolar"
        elif dönüştürülmesi_istenen_döviz == "3" :
            dönüştürülmesi_istenen_döviz = "Euro"
        elif dönüştürülmesi_istenen_döviz == "4" :
            dönüştürülmesi_istenen_döviz = "Sterlin"
        else :
            print("Lütfen geçerli bir döviz nuamrası seçin")
            continue
        break
    Türk_lirası = 1 
    Dolar = 42.70
    Euro = 50.12
    Sterlin = 57.16
    döviz_miktarı = int(input(f"Kaç {dönüştürülecek_döviz}'i {dönüştürülmesi_istenen_döviz}'e çevirmek istersin?"))
    if dönüştürülecek_döviz == "Türk lirası":
        dönüştürülecek_döviz = Türk_lirası
    elif dönüştürülecek_döviz == "Dolar":
        dönüştürülecek_döviz = Dolar
    elif dönüştürülecek_döviz == "Euro":
        dönüştürülecek_döviz = Euro
    elif dönüştürülecek_döviz == "Sterlin":
        dönüştürülecek_döviz = Sterlin
    
    if dönüştürülmesi_istenen_döviz == "Türk lirası":
        dönüştürülmesi_istenen_döviz = Türk_lirası
    elif dönüştürülmesi_istenen_döviz == "Dolar":
        dönüştürülmesi_istenen_döviz = Dolar
    elif dönüştürülmesi_istenen_döviz == "Euro":
        dönüştürülmesi_istenen_döviz = Euro
    elif dönüştürülmesi_istenen_döviz == "Sterlin":
        dönüştürülmesi_istenen_döviz = Sterlin
    print((dönüştürülecek_döviz / dönüştürülmesi_istenen_döviz) * (döviz_miktarı))
    
while True :
    Döviz_dönüştürücü()
    çıkmak_ister_misin = input("Çıkmak için q tuşuna basın, devam etmek için herhangi başka bir tuş")
    if çıkmak_ister_misin != "q" :
        continue
    else:
        if çıkmak_ister_misin == "q":
            break
