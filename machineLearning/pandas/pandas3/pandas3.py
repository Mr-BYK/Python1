import pandas as pd

#SORULAR
# İMDB DATASET.CSV dosyası baz alınmıştır
df=pd.read_csv("imdb.csv")

#1-Soru: Dosya hakkında bilgileri gösteriniz
result=df
result = df.columns
result=df.info

#2-Soru: Ilk 5 kaydı gösteriniz
result=df.head()

#3-Soru: Ilk 10 kaydı gösteriniz
result=df.head(10)

#4-Soru: Son 5 kaydı gösteriniz
result=df.tail()

#5-Soru: Son 10 kaydı gösteriniz
result=df.tail(10)

#6-Soru: Sadece Movie_Title sütununu gösteriniz.
result=df["Movie_Title"]

#7-Soru: Sadece Movie_Title sütununu içeren ilk 5 kaydı gösteriniz.
result=df["Movie_Title"].head()

#8-Soru: Sadece Movie_Title ve Rating  sütunlarının ilk 5 kaydı gösteriniz.
result=df[["Movie_Title","Rating"]].head()

#9-Soru: Sadece Movie_Title ve Rating  sütunlarının son 7 kaydı gösteriniz.
result=df[["Movie_Title","Rating"]].tail(7)

#10-Soru: Sadece Movie_Title ve Rating  sütunlarının ikinci 5 kaydı gösteriniz.
result=df[["Movie_Title","Rating"]][5:10].head()

#11-Soru: Sadece Movie_Title ve Rating  sütunlarını içeren ve imdb puanı 8.0
# ve üstünde olan kayıtlardan ilk 50 tanesini getiriniz
 result=df[(df["Rating" >= 8.0 ]) & df["Rating","Movie_Title"]].head(50)

#12-Soru: Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz.
result=df[(df["YR_Released"] >=2014) & (df["YR_Released"] <=2015)][["Movie_Title","YR_Released"]]

#13-Soru: Değerlendirme sayısı (Num_Reviews) 100.000 den büyük ya da imdb puanı
# 8 ile 9 arasında olan fimleri listeleyiniz
result=df[(df["Num_Reviews"] >= 100000 | ((df["Rating"] >= 8) & (df["Rating"] <= 9)))][["Movie_Title","Num_Reviews","Rating"]]

print(result)
print(df.columns)