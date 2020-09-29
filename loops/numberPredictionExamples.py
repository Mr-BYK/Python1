"""
1.UYGULAMA:
1-100 arasında rastgale üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalısın.(hak=5)
--"random modülü" için "phyton random" şeklinde arama yapın.
--100 üzerinden puanlama yapın .Her soru 20 puan.
--Hak bilgisini kullanıcıdan alın ve her soru belirten can sayısı üzerinden hesaplayınız.
"""
"""
import random
sayi=random.randint(1,10)
can=int(input("Kaç hak kullanmak istersiniz:"))
hak=can
sayac=0
while hak>0:
   hak-=1
   sayac+=1
   tahmin=int(input("Tahmin: "))
   if sayi==tahmin:
       print(f"Tebrikler {sayac}. defada bildiniz.Toplam puanınız:{100-(100/can)*(sayac-1)}")
       break
   elif sayi>tahmin:
       print("Yukarı")
   else:
        print("Aşağı")

   if hak == 0:
       print(f"Hakkınız bitti.Tutulan sayi:{sayi}")
"""

"""
2.UYGULAMA
Girilen bir sayının asal olup olmadığını bulun.
--Asal sayı 1 ve kendisi hariç tüm böleni olmayan sayıalara denir.
"""
# 1.Yol
"""
sayi=int(input("Bir sayı giriniz:"))
if sayi == 2 or sayi == 3 or sayi == 5 or sayi == 7:
   print(f"{sayi} sayısı asaldır "),
elif sayi % 2 == 0 or sayi % 3 == 0 or sayi % 5 == 0 or sayi % 7 == 0 or sayi == 1 :
   print(f"{sayi} sayısı asal değildir ")
else:
   print(f"{sayi} sayısı asaldır ")

"""
# 2.Yol
"""
sayi = int(input("sayi"))
asalmi=True
if sayi==1:
   print("1 sayısı asal değildir")
for i in range (2 , sayi):
   if(sayi % i ==0):
       asalmi= False
       break
if asalmi:
   print("Sayısı asaldır.")
else:
   print("Sayısı asal değildir")
"""


"""
1.UYGULAMA:
1-100 arasında rastgale üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalısın.(hak=5)
--"random modülü" için "phyton random" şeklinde arama yapın.
--100 üzerinden puanlama yapın .Her soru 20 puan.
--Hak bilgisini kullanıcıdan alın ve her soru belirten can sayısı üzerinden hesaplayınız.
"""
"""
import random
sayi=random.randint(1,10)
can=int(input("Kaç hak kullanmak istersiniz:"))
hak=can
sayac=0
while hak>0:
   hak-=1
   sayac+=1
   tahmin=int(input("Tahmin: "))
   if sayi==tahmin:
       print(f"Tebrikler {sayac}. defada bildiniz.Toplam puanınız:{100-(100/can)*(sayac-1)}")
       break
   elif sayi>tahmin:
       print("Yukarı")
   else:
        print("Aşağı")

   if hak == 0:
       print(f"Hakkınız bitti.Tutulan sayi:{sayi}")
"""

"""
2.UYGULAMA
Girilen bir sayının asal olup olmadığını bulun.
--Asal sayı 1 ve kendisi hariç tüm böleni olmayan sayıalara denir.
"""
# 1.Yol
"""
sayi=int(input("Bir sayı giriniz:"))
if sayi == 2 or sayi == 3 or sayi == 5 or sayi == 7:
   print(f"{sayi} sayısı asaldır "),
elif sayi % 2 == 0 or sayi % 3 == 0 or sayi % 5 == 0 or sayi % 7 == 0 or sayi == 1 :
   print(f"{sayi} sayısı asal değildir ")
else:
   print(f"{sayi} sayısı asaldır ")

"""
# 2.Yol
"""
sayi = int(input("sayi"))
asalmi=True
if sayi==1:
   print("1 sayısı asal değildir")
for i in range (2 , sayi):
   if(sayi % i ==0):
       asalmi= False
       break
if asalmi:
   print("Sayısı asaldır.")
else:
   print("Sayısı asal değildir")
"""


