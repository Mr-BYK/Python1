#OS Modülü
import os

result=os.name # ---> nt windows işletim sistemi kullandığımızı gösterir
""" ---Dizin Değistirme--- """
os.chdir('C:\\')
os.chdir('../..')

""" ---Klasör Oluşturma--- """
os.mkdir("yeniklasör")
os.makedirs("yeniklasör2")

""" ---Etkin Dizin Öğrenme--- """
result=os.getcwd() # ---> içini doldurduğun dosyanın nerde kayıtlı olduğunu gösterir
print(result)

""" ---Listeleme--- """
result=os.listdir()
for dosya in os.listdir():
    if dosya.endswith(".py"): # .py ile biten dosyaları gösterir
        print(dosya)


""" ---Klasör Hakkında Bilgi Sahibi Olma--- """
result=os.stat("Os_Modul.sln")

result=result.st_size/1024
print(f"dosyanın işlem boyutu {result} byte")

result=DosyaAdi.DosyaAdi.fromtimestamp(result.st_ctime) # Oluşturulma tarihi
result=DosyaAdi.DosyaAdi.fromtimestamp(result.st_atime) # Son erişimle tarihi
result=DosyaAdi.DosyaAdi.fromtimestamp(result.st_mtime) # Değiştirilme tarihi


os.system("notepad.exe") #İstedğimiz aracı çalıştırırız.
os.rename("yenidosya","Yeni Klasör") # 'yenidosya' ismindeki klasörün ismini 'Yeni Klasör' yaptık.
os.rmdir("Yeni Klasör") # Yeni Klasörü sildik
os.removedir("DosyaAdi/DosyaAdi2") #Alt dizine kadar he şeyi siler

result=os.path.abspath("Os_Modul.sln") # Bu dosyanın tam konumunu bize verir
result=os.path.dirname(os.path.abspath("Os_Modul.sln")) # dosyanın tam dizinini bize verir
result.os.path.exists("Os_Modul.sln") # Bu dosyanın olup olmadığını bize gösterir