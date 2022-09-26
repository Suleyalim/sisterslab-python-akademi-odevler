#Aklından bir sayı tut oyununu yazmanızı istiyoruz. 0-100 arasında bir sayı alacak doğru tahmini yapana kadar klavyeden tahminde bulunacaksınız.

import random

Randnumber = random.randint(0, 100)

while True:
    number =int(input("0-100 arasinda bir sayi giriniz: (cikmak icin -1)"))

    if number == -1:
        print("Oyundan cikis yaptiniz")
        break    
    elif number > Randnumber:
        print("Daha kucuk bir sayi giriniz")
    elif number < Randnumber:
        print("Daha buyuk bir sayi giriniz")
    else:
        print(f"Tebrikler sayiyi tahmin ettiniz!\nSayi {Randnumber}")
    
