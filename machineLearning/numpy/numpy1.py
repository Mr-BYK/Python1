import numpy as np
"""
result = np.array([1,3,5,7,9])
result = np.arange(1,10)
result = np.arange(1,100,2) # 1den yüze kadar 2 ser arayla sayı üretir
result=np.linspace(0,5,5) # 0 dan 5 e kadar 5 eşit parçaya
result=np.random.randint(0,10)
result=np.random.randint(1,10,3) # 1 den 10 kadar 3 tane random sayı üretir
result=np.random.randn(5) #0 dan eksi değerler dahil 1 e kadar sayı üretir
result=np.random.random(5) #0 dan  1 e kadar sayı üretir
result=np.arange(50) # 0 dan 49 a kadar dizi olusturur
result=np_array.reshape(5,10) # 0 dan 49 a kadar 5 e 10luk matris olusturur
np_array=np.arange(50)
np_multi=np_array.reshape(5,10)
print(np_multi.sum(axis=0)) #sütunların toplamı
print(np_multi.sum(axis=1)) #satırların toplamı
print(np_array)
rnd_numbers=np.random.randint(1,100,10)
print(rnd_numbers)
result=rnd_numbers.max() #Dizideki en büyük değeri verir
result=rnd_numbers.min( #Dizideki en küçük değeri verir)
result=rnd_numbers.mean() #Dizinin ortalama  değerini verir
result=rnd_numbers.argmax() #Dizinin en büyük elemaının index numarasını verir
result=rnd_numbers.argmin() #Dizinin en küçük elemaının index numarasını verir

re=("-")*250
print(re)
"""


#-------------------------------------------------------------------------------------
numbers=np.array([0,5,10,15,20,25,50,75])
"""
result=numbers[5] #5.indeksi getirir
result=numbers[-1] #En son indeksi getirir
result=numbers[0:3] #0 dan 2 ye  kadar indeksleri getirir
result=numbers[:3]  #0 dan 2 ye  kadar indeksleri getirir
result=numbers[3:]  #3 den sonuna kadar bütün indeksleri getirir.
result=numbers[::]  #Bütün indeksleri getirir
result=numbers[::-1] #Bütün dizeyi ters şekilde getirir
numbers2=np.array([[0,5,10],[15,20,25],[50,75,85]])
result=numbers2 #Matrisi bastırır
result=numbers2[0] #Matrisin ilk indeksini bastırır
result=numbers2[0,0] #Matrisin ilk indeksindeki ilk elemanı bastırır
result=numbers2[2,1] #Matrisin ikinci indeksindeki ilk elemanı bastırır
result=numbers2[:,2] #Matrislerin son hanesindeki elemanları getirir
result=numbers2[:,0:2] #Matrislerin ilk iki sütunundaki elemanları getirir
result=numbers2[:2,:2] #Matrislerin ilk iki satırıını ve ilk iki indeksini bastırır
print(numbers)
"""


"""
result=np.sin(numbers) #Değerlerin sinüsünü alır
result=np.cos(numbers) #Değerlerin cosinüs alır
result=np.sqrt(numbers) #Değerlerin karakökünü alır
result=np.log(numbers) #Değerlerin logaritmasını alır

"""
#Math Opertors

"""
numbers=np.random.randint(1,100,6)
numbers2=np.random.randint(1,100,6)

mnumbers1=numbers.reshape(2,3)
mnumbers2=numbers2.reshape(2,3)
print(mnumbers1)
print(mnumbers2)

result=np.vstack((mnumbers1,mnumbers2)) #1 ve 2. Matrisi yanyana ekler
result=np.hstack((mnumbers1,mnumbers2)) #1.ve 2. Matrisi Alt alta ekler

result=numbers>=50 #numbers dizisindeki elemanalar 50 den büyük eşit mi
result=numbers %2 == 0 #numbers dizisindeki elemanlar çift mi

print(numbers[result]) #Çıkan değerleri bool şeklinde bize geri gönderir
print(result)
"""


#Examples
# 1-Soru:(10,15,30,45,60) değerleri sahip numpy dizisi olusturunuz.
#result=np.array([10,15,30,45,60])

# 2-Soru:(5,15) arasındaki sayılarla numpy dizisi oluşturunuz.
#result=np.arange(5,16)

# 3-Soru: (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.
#result=np.arange(50,100,5)

# 4-Soru:10 elemanlı Sıfırlardan oluşan bir dizi oluşturunuz.
#result=np.zeros(10)

# 5-Soru: 10 elemanlı Birlerden oluşan bir dizi oluşturunuz.
#result=np.ones(10)

# 6-Soru: (0-100) arasında eşit aralıklı 5 sayı üretin.
#result=np.linspace(0,100,5)

# 7-Soru:(10,30) arasında restgale 5 tane sayı üretin.
#result=np.random.randint(10,30,5)

# 8.Soru:[-1,1] arasında 10 adet sayı üretin.
#result=np.random.randn(10)

# 9.Soru: (3x5) boyutlarında (10-50) arasında rastgale bir matris oluşturunuz.
#result=np.random.randint(10,50,15).reshape(3,5)

# 10.Soru:Üretilen matrisin satır ve sütun sayılarının toplamlarını yazınız.
matris=np.random.randint(-50,50,15).reshape(3,5)
#rowTotal=matris.sum(axis=1)
#colTotal=matris.sum(axis=0)
#print(rowTotal)
#print(colTotal)

"""
11-Soru:Üretilen matrisin en büyük,en küçük  ve  ortalaması nedir
result=matris.max()
result1=matris.min()
result2=matris.mean()
print(matris)
print(result,result1,result2)
"""

"""
12-Soru:Üretilen matrisin en büyük değerinin indeksi kaçtır:
result=matris.argmax()
result1=matris.argmin()
print(matris)
print(result)
print(result1)
"""

#13-Soru:(10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.
result1=np.arange(10,20)
#result=result1[0:3]
#print(result)

#14-Soru:Üretilen dizinin elemanlarını tersten yazdırın
#result=result1[::-1]
#print(result)

#15-Soru:Üretilen satırın ilk satırını seçiniz.
#result=matris[0]
#print(matris)
#print(result)

#16-Soru:Üretilen satırın 2. ve 3. satırdaki elemanları hangisidir
#result1=matris[1:]
#print(matris)
#print(result1)

#17-Soru:Üretilen matrisin tüm satırlarındaki ilk elemanı seçiniz
#result1=matris[:,0:1]
#print(matris)
#print(result1)

"""
18-Soru:Üretilen matrisin her bir elemanın karesini  ve karaköünü alınız.
karakok=matris**2
print(karakok)
result1=matris[:]
result1=np.sqrt(matris)
print(matris)
print(result1)
"""
#19-Soru:Üretilen matris elemanlarının hangisi pozitif çift sayıdır?
#Aralığı (-50,+50) arasında yapınız.
#ciftler=matris[matris % 2 == 0]
#result=ciftler[ciftler>0]
#print(result)