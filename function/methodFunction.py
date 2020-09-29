
#1.Soru:Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonskiyonu yazınız.
"""
def yazdir(kelime,adet):
   print(kelime*adet)
yazdir("Kelime \n",10)
"""

#2.Soru:Kendine gönderilen sınırsız sayidaki parametreyi bir listeye yazınız.
"""
def listeyeCevir(*params):
   liste=[]

   for param in params:
       liste.append(param)
       return liste
result=listeyeCevir(10,20,30,"Merhaba")
print(result)
"""

#3.Soru:Kendisine gönderilen bir sayının tam bölenlerini bir liste halinde yazınız
"""
def tamBolenleriBul(sayi):
   tamBolenler=[]

   for i in range(2,sayi):
       if(sayi % i==0):
           tamBolenler.append(i)
   return tamBolenler
print(tamBolenleriBul(20))
"""

#4.Soru:Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
"""
def asalSayilariBul(sayi1,sayi2):
   for sayi in range(sayi1,sayi2+1):
       if sayi >1:
            for i in range(2,sayi):
               if (sayi % i == 0):
                   break
            else:
                print(sayi)
sayi1=int(input('sayı 1: '))
sayi2=int(input('sayi 2: '))

asalSayilariBul(sayi1,sayi2)

"""



