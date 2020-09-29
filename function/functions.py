#Faktöriyel Alma
def factorial(number):
   def inner_factorial(number):
       if not isinstance(number,int):
           raise TypeError("Integer bir değer girin:")

       if not number >=0:
           raise ValueError("0 dan büyük değer girin")

       if number <=1:
           return 1

       return number * inner_factorial(number - 1)
   return inner_factorial(number)
try:
   print(factorial(-1))
except Exception as ex:
   print(ex)


"""
# ÜS ALMA

def usalma(number):
    def inner(power):
        return number ** power

    return inner

two = usalma(2)
three = usalma(3)

print(two(3))

# 4 Islem

def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    return a / b

def islem(f1, f2, f3, f4, islemin_adi):
    if islemin_adi == "toplama":
        print(f1(2, 3))
    elif islemin_adi == "cikarma":
        print(f2(8 - 4))
    elif islemin_adi == "carpma":
        print(f3(3, 4))
    elif islemin_adi == "bolme":
        print(f3(3, 4))
    else:
        print("Geçersiz işlem")

islem(toplama, cikarma, carpma, bolme, "toplama")
islem(toplama, cikarma, carpma, bolme, "cıkarma")
islem(toplama, cikarma, carpma, bolme, "carpma")
islem(toplama, cikarma, carpma, bolme, "bolme")


"""