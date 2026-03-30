bakiye = 830231
print("Lütfen 4 haneli şifrinizi girin!")
şifre = (input("Şifrenizi girin:"))
if len(şifre) != 4 :
    print("Lütfen 4 haneli bir şifre girin!")
else :
    print("İşlemler :\n\n1.Para çekme \t 2.Para yatırma \n\n3.Bakiye inceleme \t 4.Para gönderme\n")
    while True:
        işlem_numarası= int(input("Yapmak istediğiniz işlemin numarasını girin:"))
        if işlem_numarası == 1 :
            çekilecek_miktar = int(input("Çekilcek miktarı yazın:"))
            while bakiye <= çekilecek_miktar :
                print("Bakiye yetersiz!")
                print(f"Bakiyeniz : {bakiye}")
                çekilecek_miktar = int(input("Çekilcek miktarı yazın:"))
                continue
            print("Paranız veriliyor...")
            print("Kalan bakiyeniz:", bakiye - çekilecek_miktar)
        elif işlem_numarası == 2 :
            yatırılacak_miktar = int(input("Yatırılacak miktarı yazın:"))
            print("Paranız yatırılıyor...")
            print("Güncel bakiyeniz:", bakiye + yatırılacak_miktar)
        elif işlem_numarası == 3 :
            print(f"Güncel bakiyeniz :{bakiye}TL")
        elif işlem_numarası == 4 :
            gönderilicek_kişinin_ibanı = input("Lütfen para göndermek istdiğniz kişinin ibanını yazınız:")
            gönderilicek_kişinin_adı_soyadı = input("Lütfen para göndermek istdiğniz kişinin adını soyadını yazınız:")
            gönderilicek_miktar = int(input("Gönderilicek miktarı yazınız:"))
            while bakiye <= gönderilicek_miktar :
                print("Bakiye yetersiz!")
                print(f"Bakiyeniz : {bakiye}")
                break
            else :
                print(f"Gönderilecek kişinini ibanı: {gönderilicek_kişinin_ibanı}\n Gönderilecek kişinin adı soyadı: {gönderilicek_kişinin_adı_soyadı}\n Gönderilecek miktar : {gönderilicek_miktar}")
                print("Paranız başarıyla gönderildi, bizi tercih ettiğiniz için teşekkürler!")
        continue
