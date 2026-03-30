def Palindrom_sayılar() :
    x = input("Lütfen kontrol etmek istediğiniz sayıyı giriniz   ")
    listx = list(x)
    tersx = list(reversed(listx))
    if listx == tersx :
        print("Bu sayı palindrom!")
    else:
        print("Bu sayı polindrom değil")

Palindrom_sayılar()
