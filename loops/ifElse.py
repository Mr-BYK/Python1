"""
1- Kullanaıcıdan isim yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
    Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralaığına karşılık
    gele not bilgisini yazdrınız.
    0-24    =>0
    25-44   =>1
    45-53   =>2
    55-69   =>3
    70-84   =>4
    85-100  =>5

3-Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilerine göre hesaplayınız.
    1.Bakım =>1.yıl
    2.Bakım =>2.yıl
    3.Bakım =>3.yıl
    **
    süre hesabını alınan gün,ay,yıl bilgisine göre gün bazlı hesaplayınız.
    (simdi) - (2018/8/1) => gün
4- Girilen bir sayının  0-100 arasında olup olmadığını kontrol ediniz.
5- Girilen bir sayının pozitif ve  çift sayı olup olmadığını kontrol ediniz.
6- Email ve parola bilgileri ile giriş kontrolü yapınız.
7- girilen 3 sayıyı büyük olanı karşılaştırınız.
8 -Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
        Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
        a-) Ortalma 50 olsa bile final notu en az 50 olmalıdır.
        b-) Finadlen 70 alındığında ortalamının önemi olmasın.
"""
#1.Soru:
"""
isim=input("Adınızı giriniz:")
yas=int(input("Doğum tarihinizi giriniz:"))
egitim=input("Eğitim durumunuzu giriniz:")
sonuc=2020-yas
if(sonuc>=18) and (egitim == "lise") or(egitim == "üniversite"):
   print(f"{isim} adlı şahış yaşı tuttuğundan ve eğitim durumu yeterli seviye olduğu için  ehliyet alabilir.")
elif (sonuc < 18):
   print(f"{isim} adlı şahış yaşı tutmadığından dolayı ehliyet alamaz.")
else:
     print("Eğitim durumunuz yeterli olmadığından dolayı ehliyet alamazsınız.")
"""

#2.Soru:

yazili1=(int(input("1.yazılı notunuzu giriniz:")))
yazili2=(int(input("2.yazılı notunuzu giriniz::")))
sozlu=(int(input("Sözlü notunuzu giriniz::")))
ortalama=((yazili1+yazili2+sozlu) /3)
if (ortalama >= 0) and  (ortalama <25):
   print(f"Ortalamanız: {ortalama}  Notunuz: 0")
elif (ortalama >= 25 ) and  (ortalama <45):
   print(f"Ortalamanız: {ortalama}  Notunuz: 1")
elif ( ortalama >= 45) and  (ortalama <55):
   print(f"Ortalamanız: {ortalama}  Notunuz: 2")
elif ( ortalama >= 55) and  (ortalama <70):
   print(f"Ortalamanız: {ortalama}  Notunuz: 3")
elif ( ortalama >= 70) and  (ortalama <84):
   print(f"Ortalamanz: {ortalama}   Notunuz: 4")
elif ( ortalama >= 85) and  (ortalama <101):
   print(f"Ortalamanz: {ortalama}   Notunuz: 5")
else:
    print("Geçersiz İşlem Yapıldı")


#3.Soru:
"""
import datetime
tarih=input("aracınız hangi tarihte trafiğe çıktı (2019/8/9):")
tarih=tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi=datetime.datetime.now()
fark=(simdi-trafigeCikis)
days=fark.days

if days<=365:
   print("1.servis aralığı")
elif days>365 and days>=365*2:
   print("2.servis aralığı")
elif days>365*2 and days<=365*3:
   print("3.servis aralığı")
else :
   print("hatalı süre")
"""

#4.Soru:
"""
sayi=int(input("Bir sayı giriniz:"))
print(sayi)
if ( sayi > 0) and (sayi <=100):
   print(f"Girdiniz sayının değeri: {sayi} \n 0 ile 100 arasındadır.")
else:
   print(f" Girdiniz sayının değeri: {sayi} \n 0 ile 100 arasında değildir.")
"""

#5.Soru:
"""
sayi=int(input("Bir sayı giriniz:"))
print(sayi)
if (sayi>0) :
   print("Girdiğiniz sayı pozitiftir.")
   if (sayi /2 == 0):
       print("Girdiğiniz sayı pozitif ve çifttir .")
   else:
       print("Girdiğiniz sayı çifttir değidlir .")
else:
    print("Giediğiniz ayı negatiftir.")
"""

#6.Soru:
"""
Email="yusuf"
Parola="123"
GirilenEmail=(input("Bir email giriniz:"))
GirilenParola=str(input("Bir parola giriniz:"))
if  (GirilenEmail==Email):
          if (GirilenParola==Parola):
              print("Girişiniz başarılı.")
          else:
             print(" Password - Girişiniz başarısız.")
else:
   print("Email - Girişiniz başarısız.")
"""

#7.Soru:
"""
sayi1=int(input("1.Sayı giriniz:"))
sayi2=int(input("2.Sayı giriniz:"))
sayi3=int(input("3.Sayı giriniz:"))
if (sayi1>sayi2) and (sayi1>sayi3):
   print(f"{sayi1} değerindeki sayi en büyüktür.")
elif (sayi2>sayi1) and (sayi2>sayi3):
   print(f"{sayi2} değerindeki sayi en büyüktür.")
elif (sayi3>sayi1) and (sayi3>sayi2):
   print(f"{sayi3} değerindeki sayi en büyüktür.")
else:
   print("Geçersiz değer")
"""

#8.Soru:
"""
vize1=(float(input ("1.Vize notunuzu giriniz:")))
vize2=(float(input ("2.Vize notunuzu giriniz:")))
final=(float(input ("Final notunuzu giriniz:")))
ortalama=(vize1*0.3)+(vize2*0.3)+(final*0.4)
durum=(ortalama >=50) and (final>=50)
durum=(ortalama >=50) or (final >=70)
if(ortalama >=50):
    print(f"Öğrencinin ortalaması :{ortalama} ve geçme durumu : BAŞARILI")
else:
    if (final>=70):
        print(f"Öğrencinin ortalaması :{ortalama} ve geçme durumu : BAŞARISIZ")
    else:
        print(f"Öğrencinin ortalaması :{ortalama} ve geçme durumu : BAŞARISIZ")
"""
