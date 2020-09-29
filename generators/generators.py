def cube():
    for i in range(5000):
        yield i ** 10 #bellek üzerinde yer kaplamadan işlem yaptırırız.İkinci kez ulasılmaz bir kereye masustur
for i in cube():
    print(i)

##mesela bellek üstüned nasıl yer kaplar
#def cube():
#    result=[]

#    for i in range(5):
#        result.append(i**3)
#        return result
#print(cube())

generator=(i**3 for i in range(5))
print(generator)

#print(next(generator))
#print(next(generator))
#print(next(generator))
for i in generator:
    print(i)