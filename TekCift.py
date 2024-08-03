try:
    
    sayi = int(input("Bir sayı girin: "))
    
    secim = str(input("Tek mi yoksa çift mi toplamak istiyorsunuz? (tek/çift): "))
    
    toplam = 0
    
    if secim == "tek":
        for i in range(1, sayi + 1):
            if i % 2 != 0:
                toplam += i
    elif secim == "çift":
        for i in range(1, sayi + 1):
            if i % 2 == 0:
                toplam += i
    else:
        raise ValueError("doğru veri tipi giriniz lütfen.")
    
    
    print(f"Toplam: {toplam}")

except ValueError as e:
    print(f"Hata: {e}")

except Exception as e:
    print(f"Beklenmeyen bir hata oluştu: {e}")
