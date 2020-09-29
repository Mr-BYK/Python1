"""
SORULAR
1- Bmw,Mercedes,Opel,Mazda elemanlarını sahip bir liste  oluşturunuz.
2-Liste kaç elemanlıdır?
3-Listenin ilk ve son elemanı nedir?
4 Mazda değerini toyota ile değiştirin.
5-Mercedes listenin bir elemaını mıdır?
6-Listenin -2 indeksindeki değer nedir?
7-Listenin ilk 3 elemanını alın.
8-Listenin son iki elemanı yerine Toyota ve Renault değerlerini ekleyin.
9-Listenin üzerine  Audi ve Nissan değerlerini ekleyin.
10-Listenin son elemanlarını silin.
11-Liste elemanlarını tersten yazdırın.
12- Aşağıdaki Verileri bir liste içinde saklayınız.
    StudentA: Yiğit Bilgi 2010,(70,60,70)
    StudentB: Sena Turan 1999,(80,80,70)
    StudentC: Ahmet Turan 1198,(80,70,90)
13-Liste elemanlarını ekrana yazdırınız.
14-F string metodunu kullanarak yğiyi bilgi 9 yaşında ve not ortalamasını küsuratlı şekilde yazdırın.
"""
#CEVAPLAR
#1.Soru:
#Cars=["Bmw","Mercedes","Opel","Mazda"]
#2.Soru:
#print (len(Cars))
#3.Soru:
#print(Cars[0])
#print(Cars[3])
#4.Soru:
#Cars[3]='Toyota'
#print(Cars)
#5.Soru:
#result  = 'Mercedes' in Cars
#print (result)
#6.Soru:
#print(Cars[-2])
#7.Soru:
#print (Cars[0:3])
#8.Soru:
#Result=Cars[-2]="Toyota","Renault"
#print (Cars)
#9.Soru:
#Result=Cars+["Audi","Nissan"]
#print (Result)
#10.Soru:
#del Cars[-1]
#print (Cars)
#11.Soru:
#Result = Cars[::-1]
#print (Result)
#12-13.Soru:
StudentA = ["Yiğit","Bilgi",2010,[70,60,70]]
StudentB = ["Sena", "Turan",1999,[80,80,70]]
StudentC = ["Ahmet","Turan",1198,[80,70,90]]
print(StudentA)
print(StudentB)
print(StudentC)
#14.Soru:
print(f"{StudenA[0]} {StudenA[1]} {2019-StudenA[2]} yaşında ve not ortalamsı {(StudenA[3][0] + StudenA[3][1] + StudenA[3][2])/3}" )