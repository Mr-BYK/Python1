"""
print("Öğrenci adınızı giriniz:")
OgrenciAdi=input()
print("Öğrenci soyadınızı giriniz:")
OgrenciSoyAd=input()
print ("Okul numaranızı girin:")
OkulNo=input()
print ("Telefon numamarınzı giriniz:")
TelefonNo=input()
liste=[]
liste.append("Öğrenci adınızı giriniz:\n"+[OgrenciAdi]+[OgrenciSoyAd]+[OkulNo]+[TelefonNo])
print(liste)

ogrenciler={}
number=input("öğrenci no:")
name=input("öğrenci adı:")
surname=input("öğrenci soyadı:")
phone=input("öğrenci telefon:")
ogrenciler[number]={
    'ad':name,
    'soyad':surname,
    'telefon':phone
    }
print (ogrenciler)

ogrenciler.update({
    number:{
        'ad':name,
        'soyad':surname,
        'telefon':phone
        }
    })
number=input("öğrenci no:")
name=input("oğrenci adı:")
surname=input("öğrenci soyad:")
phone=input("öğrenci telefon:")

ogrNo=input('öğrenci no:')
ogrenci=ogrenciler[ogrNo]

print(f"Aradığınız {'ogrNo'} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")

"""
liste =["1","2","5a","10b","abc"]

#1-Liste elemanları içindeki sayısal değerleri bulunuz.
for x in liste:
    try:
         result =int(x)
         print (result)
    except ValueError:
         continue