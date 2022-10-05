'''
Sayı Tahmin Oyunu
* Random modülü ile bir sayı alınır
* guess adında bir fonksiyon yazılacak
* input ile kullanıcıdan tahminde bulunması istenip ardından yönlendirmeler yapılacak
'''

from random import randint

def tahmin(number):
    user_number = int(input("Oyun için 1-200 arasında bir tahminde bulununuz: "))
    while number != user_number:
        if number < user_number:
            print("üzgünüm, daha küçük bir tahminde bulunmalısın. ")
        else:
            print("üzgünüm, daha büyük bir tahminde bulunmalısın. ")
        user_number = int(input("Lütfen yeni bir tahminde bulununuz! "))
    else:
        print("Tebrikler, doğru tahmin! ")
tahmin(randint(1, 200)) 