#Kayıp ve Bozuk Veri Analizi

import pandas as pd
import numpy as np

data=np.random.randint(10,100,15).reshape(5,3)
df=pd.DataFrame(data,index=['a','c','e','f','h'],columns = ['column1','column2','column3'])

df=df.reindex(['a','b','c','d','e','f','g','h'])
newColumn=[np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"]=newColumn

result=df
result=df.drop("column1",axis=1) # sütun1 siler
result=df.drop(["column1","column2"],axis=1) #sütun 1 ve 2 yi siler  sütun silmek istersek axis=1 dememiz lazım
result=df.drop("a",axis=0) #a satırını siliyoruz axis=0 diyerek satırı belirtiyoruz
result=df.drop(["a","b","d","h"],axis=0)

result=df.isnull() #Boş değerleri gösterir
result=df.notnull() #Dolu değerleri gösterir
result=df.isnull().sum() #Boş değerleri sayar
result=df["column1"].isnull().sum() #sütun1deki boş değerleri sayar
result=df[df["column1"].isnull()]["column1"] #Sütun1 deki nan değerleri gösterir
result=df[df["column1"].notnull()] #Sütun1 deki boş olmayan değerleri getiriir
result=df.dropna() #axis = 0 satırdaki nan değerleri siler
result=df.dropna(axis=1) #axis = 1 sütundaki nan değerleri siler
result=df.dropna(how= 'any') #satıda nan değeri gördüğünde satırı siler
result=df.dropna(how='all') #tüm satırda nan değeri varsa satırı siler
result=df.dropna(subset=["column1","column2"],how="all")
result=df.dropna(subset=["column1","column2"],how="any")
result=df.dropna(thresh=1) #En az bir tane normal veri varsa kayıtları silmez
result=df.dropna(thresh=4) #En az dört tane normal veri varsa kayıtları silmez
result=df.fillna(value=1) #NaN değerlere 1  değerini verdik çünkü çarpma işleminde 1 etksisiz elemandır

result=df.sum() #sütunların toplamını verir
result=df.sum().sum() #Bütün sütunların toplamını verir
resulf=df.size #Toplam eleman sayısını verir
result=df.isnull().sum().sum() #Toplam nan değerlerini sayısını verir

def ortalama(df):
    toplam=df.sum().sum()
    adet=df.size - df.isnull().sum().sum()
    return  toplam/adet
result=df.fillna(value=ortalama(df))   #Bütün null olan yerlere hesaplanan ortalama değeri veriyoruz çünkü veri seti yanlış çıkmaması için
print(result)
