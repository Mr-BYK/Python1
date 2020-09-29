liste = ["1", "2", "5a", "10b", "abc"]
"""
# 1-Liste elemanları içindeki sayısal değerleri bulunuz.
for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue
"""

# 2-Kullanıcı 'q' değerini girmedikçe aldıgınız her inputun sayısal değeri olduğundan emin olunuz
# aksi halde hata mesajı yazınız.
"""
while True:
    sayi = input("sayı: ")
    if sayi == "q":
        break
    try:
        result = float(sayi)
        print("Girdiğiniz sayi: ", result)
    except ValueError:
        print("Geçersiz Sayı")
        continue
"""



# 3-Girilen parola içinde türkçe karakter hatası veriniz.
"""
def checkPassword(parola):
    turkcekarakterler = "şçpüöıİ"

    for i in parola:
        if i in turkcekarakterler:
            raise TypeError("Parola türkçe ifade içeremez.")
        else:
            pass
    print("geçerli parola")
"""


# 4-Faktöriyel fonskiyonu oluşturup fonksiyona gelen değer içinde hata mesajları verin.
"""
try:
   import math
   x=int(input("Bir tam sayı değeri giriniz:"))
   value = math.factorial(x)
   print(value)
except (ZeroDivisionError,ValueError,SyntaxError) as e:
   print("Uygun olmayan karakter",e)
   print(e)
else:
   print("Faktöriyeliniz",value)
"""


