try:
    x=int(input("bir sayı gir"))
except ValueError:
        print("hata")
else:
        print("hata yok")
finally:
    print("tekrar deneyin")