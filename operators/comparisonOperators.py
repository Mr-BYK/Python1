#1.Soru:Girilen 2 sayıdan hangisi büyüktür?
"""
a=int(input('a:'))
b=int(input('b:'))
result=(a>b)
print(f'a: {a} b: {b} den büyüktür:{result}')
"""

# 2.Soru:Kullanıcıdan 2 vize(%60) ve final (%40) notunu alıp ortalamyı hesaplayınız.
"""
vize1=float(input("1. Vize notunuzu giriniz:"))
vize2=float(input("2. Vize notunuzu giriniz:"))
final=float(input("Final notunuzu giriniz:"))
ortalama= (vize1*0.3)+(vize2*0.3)+(final*0.40)
ortalama>=50
print(f'not ortalamanız:{ortalama} ve dersten geçme durumunuz:{ortalama>=50} ')
"""

#3.Soru:Girilen bir sayının tek mi çiftmi olduğunu yazdırın.
"""
sayi=int(input("Bir sayi giriniz:"))
tekcift =sayi % 2 == 0
print(f'Girilen sayının çift olma durumu :{tekcift}')
"""

#4.Soru:Girilen bir sayının negatif pozitif durumunu yazdırın.
"""
sayi=int(input("Bir sayi giriniz:"))
negatifpozitif=sayi>0
print(f'Girdiğiniz sayı {sayi}  pozitif mi:{negatifpozitif}')
"""

#5.Soru:Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
        # (email:email@sadikturan.com parola:abc123)
"""
Email="yusuf"
Parola:123
GirilenEmail=(input("Bir email giriniz"))
isEmail=(Email==GirilenEmail)
GirilenParola=(input("Bir parola giriniz"))
İsparola=(Parola==GirilenParola)
print(f"Email bilgisi doğru mu?{isEmail} ve Parola Doğru mu? {İsparola} ")
"""

