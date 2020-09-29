#Regular Expression - Düzenli Ifade
import re
#str =" Iyinin ve kötünün ardında bir yer var | seninle  orada bulaşacağız"
#result=re.findall("Iyinin",str)
#result=len(result) #---> Aradğımız ifadeden kaç tane bulduğumuzu gösterir

#re.split()
#result=re.split(" ",str) #---> Bosluk ifadelerini böl
#result=re.split("o",str) #---> O harfiden sonra böler

#re.sub()
#result=re.sub(" ","-",str) #---> Bütün boşluk karakterlerini - ile değiştiriyoruz
#result=re.sub("\s","-",str) #---> Bütün boşluk karakterlerini - ile değiştiriyoruz

#re.search()
#result=re.search("Iyinin",str) #---> Aranan kelimeyi match objesi olarak bulur
#result=result.span() #---> Aranan ifadenin ilk ve son karakterini bastırır.
#result=result.start() #---> Aranan ifadenin ilk karakterini bastırır.
#result=result.end() #---> Aranan ifadenin son karakterini bastırır
#result=result.group() #---> Aradığı ifadeyi bastırır.
#result=result.string() #---> Aradığı string ifadeyi bastırır.

"""
[a-e] =>[abcde]  ---> A dan e ye kadar arar
[1-5] =>[12345]  ---> 1 den 5 e kadar arar
[0,39] =>[123]  ---> 0 dan 3 kadar arar

[^abc] =>abc dışındaki karakterleri arar
[^0-9] =>rakam olmayan karakterler
. --> her hangi bir karakteri ifade eder.
.. --> iki basamaklı her hangi bir karaketeri ifade eder.
^a --> belirtilen ifade a ile başlıyor mu
$a --> belirtilen ifade a ile bitiyor mu
ma*n --> ma ifadesinden sonra n karakteri geliyor mu 
    maan -->geliyor
    main --> gelmiyor


{}-KArakter sayısını kontrol eder.
al{2} => a karakterinin arkasına 1 karakteri 2 kez tekrarlamalı.
al{2,3} => karakterinin arkasına 1 karakteri en az 2 en fazla 3 kez tekrarlamalı
[0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.

()-gruplandırmak için kullanılır.
 (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.

 \ - Özel karakterleri aramamızı sağlar.
    \$a => karakterlerinin arkasına a karakterini arar.
    Yani $ a regular exp. engine tarafından yorumlanmaz.

\A - Belirtilen karakterler string in başında mı
    \Athe => The string in başında mı

\Z - Belirtilen karakterr string in sonunda mı?
    \bthe => the kelime in başında mı
    the\b => the kelime in sonunda değil mi

\B-Belirtilen karakter kelimenin in başında ya da sonunda değil mi
    \Bthe => the kelimenin in başında değil mi
    the\B => the kelimenin in sonunda değil mi

\d - [0-9] ile aynı anlama gelir yani rakamları arar.
    \d => 12abc34

\D - [^0-9] ile aynı anlama gelir ysni rakam olmayanları arar.
    \D => 1ab44_50

\s - Boşluk karakterlerini arar
\S - Boşlun karakterlerinin dışındakini arar.
\w - Alfabetik karakterşer, rakamlar ve alt çizgi karakteri
\W - \w nin tam tersi

arama metodu result=re.findall("[ \parametre aranacak karakter]",str)
Detaylı bilgi için python regEx
"""


"""
result=re.findall("[abc]",str)
result=re.findall("[sat]",str)
result=re.findall("[a-e]",str)
result=re.findall("[a-z]",str) 
result=re.findall("[0-5]",str) 
print(result)
"""
