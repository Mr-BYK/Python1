
x, y, z = 2, 5, 10
numbers= 1 ,5 ,7 ,10 ,6

#1.Soru: Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z, toplamının farkı nedir?
"""
a = int (input('1.sayiyi girin:'))
b = int (input('2.sayiyi giriniz.'))
result= (a*b)-(x+y+z)
print(result)
"""

#2.Soru: y' nin x' kalansız bölümünü hesaplayınız.
"""
result=y//x
print(result)
"""

#3.Soru: (x,y,z) toplamının mod 3'ü nedir?
"""
result=(x+y+z)%3
print(result)
"""

#4.Soru:  y' nin x. kuvvetini hesaplayınız.
"""
result=y**x
print(result)
"""

#5.Soru: x,*y,z=number işlemine göre z' küpü kaçtır?
"""
x, *y, z=numbers
result=z**3
print(result)
"""

#6.Soru: x,*y,z =numbers işlemine göre y nin değerini toplamı kaçtır?
"""
x,*y, z=numbers
result = y[0]+y[1]+y[2]
print(result)
"""
