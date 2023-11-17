import random
def sayi_uret():
    return random.randint(1, 10)  

uretilen_sayi = sayi_uret()

tahmin = int(input("1 ile 10 arasında bir sayı tahmin edin: "))

if tahmin == uretilen_sayi:
    print("Tebrikler! Doğru tahmin ettiniz.")
else:
    print(f"Üzgünüm, doğru sayı {uretilen_sayi}. Tekrar deneyin.")

