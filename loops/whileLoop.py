#1.Soru:Sayılar listesini while ile ekrana yazdırın.

"""
sayilar=[1,3,5,7,9,12,19,21]
while sayilar :
   print(sayilar)
"""
#2.Soru:Başlangıç be bitiş değerlerini kullanıcıdan aradaki tüm tek sayıları ekrana yazdırın.
"""
baslangic=(int(input("Bir başlangıç değeri giriniz:")))
bitis=(int(input("Bir bitiş değeri giriniz:")))
i=baslangic
while i < bitis:
   i+=1
   if(i % 2 == 1 ):
       print(i)
print("Bitti")
"""

#3.Soru:1-100 arasındaki sayıları azalan şekilde yazdırın.
"""
i = 100
while i > 0:
   print(i)
   i-=1
"""

#4.Soru:Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
"""
numbers=[]
x=0
while x<5:
   sayi=int(input("sayi"))
   numbers.append(sayi)
   x+=1
numbers.sort()
print(numbers)
"""


"""
# 5:Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayınız.
#        -- ürün sayısını kullanıcıya sorun
#        -- dictionary listesi yapısı (name,price) şeklinde olsun.
#        -- ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.


urunler =  []
adet = int(input("Kaç adet eklemek istiyorsunuz:"))
i=0
while (i < adet ):
   name = input("ürün ismi:")
   price = input("ürün fiyatı:")
   urunler.append({
       "name":name,
       "price": price
       })
   i +=1
for urun in urunler:
    print(f'ürün adı: {urun["name"]} ürün fiyatı:{urun["price"]}')
"""
