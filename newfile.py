import random
def sayi_uret():
    return random.randint(1, 100)  

uretilen_sayi = sayi_uret()
hak = 5
try:
    
    
    tahmin = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
    flag=False
    while flag==False:
 
          if tahmin == uretilen_sayi:
             
             print("Tebrikler! Doğru tahmin ettiniz.")
             flag=True
          else:
            hak = hak -1
            if hak == 0:
                print("yone yanlis hakkiniz bitti defolun")
        
            print(f"Üzgünüm,,YanlışTekrar deneyin. kalan hakkiniz",hak )
            if tahmin < uretilen_sayi:
                print("daha buyuk sayi gir")
            tahmin = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
except ValueError:
    print("sacma sapan harf girme")
except:
    print("degisik bir hata")
