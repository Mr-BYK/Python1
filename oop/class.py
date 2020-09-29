# Class
class Person:
    # Class Attributes - Sınıf Öznitelikleri
    address = 'No Information'

    # Constructor(Yapıcı Metod)
    def __init__(self, name, year):
        # Object Attributes - Nesne Öznitelikleri
        self.name = name
        self.year = year

    # Instance Methods - Metod Örnekleri
    def intro(self):
        print("Hello There.I am " + self.name)

    def calculateAge(self):
        return 2020 - self.year
        # Object(Instance) - Nesne Örnekleri
        p1 = Person(name="Ali", year=1990)
        p2 = Person(name="Yağmur", year=1995)

        # Updating - Güncelleme
        p1.name = "Ahmet"
        p1.address = "Manisa"

        # Accessing Object Attributes - Nesneye Erişme Öznitelikleri
        print(f'p1:name{p1.name} year:{p1.year} adress:{p1.address}')
        print(f'p2:name{p2.name} year:{p2.year} adress:{p2.address}')

        print(f'adım:{p1.name} ve yaşım {p1.calculateAge()}')
        print(f'adım:{p2.name} ve yaşım {p2.calculateAge()}')

        p1(intro)
        p2(intro)





class Circle:
    # Class object attribute - Sınıf nesne öznitelikleri
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    # Methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap ** 2)


c1 = Circle()  # yaricap=1
c2 = Circle(5)

print(f'c1:  alanı= {c1.alan_hesapla()} çevre {c1.cevre_hesapla()}')
print(f'c2:  alanı= {c2.alan_hesapla()} çevre {c2.cevre_hesapla()}')
