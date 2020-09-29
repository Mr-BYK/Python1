#----------------------1.BÖLÜM---------------------
#DATAFRAME ile SATIR-SÜTUN SEÇİMLERİ
# import pandas as pd
# from numpy.random import randn

#df=pd.DataFrame(randn(3,3), index = ["A","B","C",], columns = ["Column1","Column2","Column3"])
"""
Seçme İşlemleri
result=df
result=df[["Column1","Column2"]] #Sütuna göre sıralama Çift Köşeli parantez !!!
result=df.loc["A"] #Satıra göre sıralama
result=type(df.loc["A"])
result=df.loc[:,["Column1","Column2"]] #Sütun 1 ve 2 yi bastırır
result=df.loc[:"B",:"Column2"] #B satırına kadar 2.sütunu getirir
"""
#Yeni Bir Satır Ekleme İşlemi
"""
df["Column4"]=pd.Series(randn(3),["A","B","C"]) #4.Sütunu ekler
df["Column5"]=df["Column1"]+df["Column3"] # 1 ve 3. sütunu toplar 5.sütuna yazar

result=df.drop("Column5",axis = 1)

print(result)
print(df)
"""

#----------------------2.BÖLÜM---------------------
#DATAFRAME ile FİLTRELEME
"""
import pandas as pd
import numpy as np
data=np.random.randint(10,100,75).reshape(15,5)
df=pd.DataFrame(data,columns = ["Column1","Column2","Column3","Column4","Column5",])

df.columns #veriseti içindeki column bilgilerini gösterir
# result=df.head(5) #İlk 5 satırı getirir
# result=df.tail(10) #Son 10 bilgiyi ekrana yazdırır,tail içi default olarak 5 değerini bastırır
# result=df["Column1"].head() #1.Sütunun ilk 5 satırını getirir
# result=df.Column1.head() #1.Sütunun ilk 5 satırını getirir
# result=df[["Column1","Column2"]].head()
# result=df[5:15][["Column1","Column2"]].head() # 5 ve 15 kayıt arasındaki ilk 2 sütunu gösterir --Parçalama İşlemi--
# result=df>50 # 50 den büyük değerleri True-False olarak verir
# result=df[df>50] #%50 den büyük değerlerin NaN ve değerini verir
# result=df[df % 2 == 0] #Çift olanları ekrana bastırır.
# result=df[df["Column1"] >50][["Column1","Column2"]
# AND ve OR İŞLEMLERİ
# result=df[(df["Column1"] >50) & (df["Column1"] <=70)]
# result=df[(df["Column1"] >50) | (df["Column2"] <=70)]
# result=df.query("Column1 >= 50 | Column1 % 2 == 0")[["Column1","Column2"]]
# result=df.query("Column1 >= 50 & Column1 % 2 == 0")[["Column1","Column2"]]
print(result)

"""
