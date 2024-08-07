try:
    number=float(input("bir sayı giriniz lütfen:"))
    
    number2=float(input("bir sayı daha giriniz lütfen:"))

    
    print("1.toplama")
    print("2.çıkarma")
    print("3.çarpma")
    print("4.bölme")
    x=float(input("lütfen bir sayı seçiniz(1/2/3/4):"))
    if x==1:
        sonuc=number+number2
        print("cevap:",sonuc)
    elif x==2:
        sonuc=number-number2
        print("cevap:",sonuc)    
    elif x==3:
        sonuc=number*number2
        print("cevap:",sonuc)
    elif x==4:
        sonuc=number/number2
        print("cevap:",sonuc)
except ValueError:
    print("hata var tekrar deneyin")
else:
    print("hata yok kod doğru")
finally:
    print("program sonlandı")
    

    
    
