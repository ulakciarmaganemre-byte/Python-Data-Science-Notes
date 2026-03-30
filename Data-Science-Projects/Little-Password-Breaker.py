şifre = input("Şifrenizi girin:")
şifre1 = int(şifre)
while True:
    sayı =random.randint(0000, 9999)
    print(sayı)
    if şifre1 == sayı:
        print("Şifreniz",sayı,"muydu?")
        break
