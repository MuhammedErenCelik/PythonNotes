sinav1=int(input("İlk sınavı girin"))

sinav2=int(input("İkinci sınavı bulunuz"))

performans=int(input("Performan Notunu giriniz"))

ortalama=(sinav1+sinav2+performans)/3

if ortalama>=50:
   print("Geçtiniz")
   
else:
    print("Kaldınız")

ortalama=round(ortalama,2)

print(ortalama)