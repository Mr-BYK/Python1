# Error Handling - Hata Yönetimi

try:
   x=int(input("x: "))
   y=int(input("y: "))
   print(x/y)
except ZeroDivisionError:
   print("y için 0 girilmez")

except ValueError:
   print("x ve y için bir sayısal değer girmelisiniz")

#2.YOL

try:
   x=int(input("x: "))
   y=int(input("y: "))
   print(x/y)
except (ZeroDivisionError,ValueError) as e :
   print("Yanlış Bilgi girdiniz")
   print(e)

#3.YOL Gelişmiş

while True:
   try:
       x=int(input("x: "))
       y=int(input("y: "))
       print(x/y)
   except Exception as ex:
       print("Yanlış Bilgi Girdiniz", ex)
   else:
       break
   finally:
       print("try except sonlandı.")

# Parola oluşturma Hata yönetimi

def check_password(psw):
   import re
   if len(psw) < 8:
       raise Exception("Parola en az 7 karakter olmalıdır.")
   elif not re.search("[a-z]",psw):
       raise Exception("Parola küçük harf içermelidir.")
   elif not re.search(["A-Z",psw]):
       raise Exception("Parola büyük harf içermelidir.")
   elif not re.search("[0-9]",psw):
       raise Exception("Parola rakam içermelidir.")
   elif not re.search("[/_@]",psw):
       raise Exception("Parola alpha numeric karakter içermelidir")
   elif re.search("\s",psw):
       raise Exception("Parola boşluk içermemelidir")
   else:
       print("Geçerli Parola")
password="123456aA_"
try:
   check_password(password)
except Exception as ex:
   print(ex)
finally:
   print("Validation tamamlandı")

