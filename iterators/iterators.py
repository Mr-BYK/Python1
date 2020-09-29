"""
liste=[1,2,3,4,5]
iterator=iter(liste)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))               # ----> for i in liste:
print(next(iterator))               # ----> print(i)
#print(next(iterator))               #6. yazdırmada hata verir ama for döngüsü vermez

#Bu şekilde hatasız amacımıza ulasırız
iterator=iter(liste)
while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break


"""

#Examples
class MyNumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x =self.start
            self.start +=1
            return x
        else:
            raise StopIteration
list=MyNumbers(10,20)
benimIter=iter(list)
print(next(benimIter))
print(next(benimIter))
print(next(benimIter))
# Kaç kere tekrarlarsan o kadar eleman yazdırılı ya da for döngüsünü kullanırız
# for x in list:
#     print(x)