
#1.Soru:Girilen bir sayının 0-100 arasında olup olmadığı kontrol ediniz.
"""
sayi= ( int(input( "Bir 0-100 arasında sayı giriniz:")))
result = (sayi >=0) and (sayi <= 100)
print(f'sayi 0- 100 arasında mı ?{result}')
"""

#2.Soru:Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
"""
sayi= ( float (input( "Bir sayı giriniz:")))
result = (sayi > 0) and (sayi % 2 == 0)
print(f'sayi pozitif ve çift mi  ?{result}')
"""

#3.Soru:Email ve parola bilgileri ile giriş kontrolü yapınız.
"""
Email="yusuf"
Parola="123"
GirilenEmail=(input("Bir email   giriniz:"))
GirilenParola=(input("Bir şifre giriniz:"))
result=(GirilenEmail== Email)  and (Parola==GirilenParola)
print(f'Uygulama giriş Başarılı mı:{result}')
"""

#4.Soru:Girilen 3 sayıyı büyüklük olarak karşılaştrınız.
"""
a=input("Bir A sayısı giriniz:")
b=input("Bir B sayısı giriniz:")
c=input("Bir C sayısı giriniz:")
result= (a>b) and (a>c)
print(f'En büyük A değeridir {result}')
result = (b> a) and (b>c)
print(f'En büyük B değeridir {result}')
result= (c>a ) and (c>b)
print(f'En büyük C değeridir {result}')
"""
""""
5- Soru:Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
    a-) ortalama 50 olsa bile final notu en az 50 olmalıdır.
    b-) Finalden 70 alındığında ortalamanın önemi olmasın.
CEVAP
Vize1 =  (int(input("Birinci Vize notunuzu giriniz:")))
Vize2 =  (int(input("İkinci Vize notunuzu giriniz:")))
Final =  (int(input("Final notunuzu giriniz:")))
ortalama=(Vize1*0.4)+(Vize2*0.4)+(Final*0.3)
print(ortalama)
result = (ortalama >= 50) and(Final>=50)
result=  (ortalama >=50) or  (Final>=70)
print(f"Öğrencinin ortalaması {ortalama} ve geçme durumu :{result}")    
"""



"""
6-Soru:Kişinin ad, kilo ve boy bilgilerini  alıp kilo indekslerini hesaplayınız.
    Formül:(Kilo/ boy uzunluğunun karesi)
    Aşağdaki tabloya göre kişi hangi gruba girmektedir.
    0-18.4      =>Zayıf
    18.5-24.9   =>Normal
    25.0-29.9   =>Fazla Kilolu
    30.0-34.9   =>Şişman(Obez)
CEVAP
"""
isim=input('Adınızı giriniz:')
kilo=float(input('Kilonuzu giriniz:'))
boy=float(input('Boyunuzu  1.80 şeklinde giriniz:'))
result= (kilo) / (boy**2)
zayıf=(result>= 0) and (result<=18.4)
normal=(result> 18.4) and (result<=24.9)
kilolu=(result> 24.9) and (result<=29.9)
obez=(result> 29.9) and (result<=34.9)
#Zayıf=(0 >= result <=18.4)
#Normal=(18.5 > result <=24.9)
#Fazla_Kilolu=(25.0 > result <= 29.9)
#Sisman_Obez=(30.0 > result <= 34.9)
print(f'{isim} isimli kişinin kilo indeksi: {result} ve değerlendirmeniz: {zayıf}')
print(f'{isim} isimli kişinin kilo indeksi: {result} ve değerlendirmeniz: {normal}')
print(f'{isim} isimli kişinin kilo indeksi: {result} ve değerlendirmeniz: {kilolu}')
print(f'{isim} isimli kişinin kilo indeksi: {result} ve değerlendirmeniz: {obez}')