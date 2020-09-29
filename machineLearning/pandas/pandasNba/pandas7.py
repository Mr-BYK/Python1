import numpy as np
import pandas as pd

"""
NBA_CSV
1- İlk 10 kaydı getiriniz
2-Toplam kaç kayıt vardır
3-Tüm oyuncuların toplam kilo ortalaması nedir
4-En yüksek kilosu ne kadardır
5-En yüksek kilosu  olan oyuncu kimdir
6-Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımı gösteriniz
7-"John Holland" isimli oyuncunun oynadığı takım hamgisidir
8-Takımlara göre oyuncuların ortalama kilo bilgisi nedir
9-Kaç farklı takım mevcut
10-Her takımda kaç oyuncu oynamaktadır
11-Ismi içinde "and" geçen kayıtları bulunuz
"""
df=pd.read_csv("nba.csv")
# 1.Soru Cevabı
result=df.head()
# 2.Soru Cevabı
result=len(df.index)
# 3.Soru Cevabı
result=df["player_weight"].mean()
# 4.Soru Cevabı
result=df["player_weight"].max()
# 5.Soru Cevabı
result=df[df["player_weight"]==df["player_weight"].max()]["player_name"].iloc[0]
# 6.Soru Cevabı
result=df[(df["age"] >= 20) &(df["age"] <25 )][["player_name","team_abbreviation","age"]]
# 7.Soru Cevabı
result=df[df["player_name"] == "John Holland"][["player_name","team_abbreviation"]]
# 8.Soru Cevabı
result=df.groupby("team_abbreviation").mean()["player_weight"]
# 9.Soru Cevabı
result=len(df.groupby("team_abbreviation"))
# 10.Soru Cevabı
result=df["team_abbreviation"].value_counts()
# 11.Soru Cevabı

# result=df[df["player_name"].str.contains("and")]
def str_find(name):
    if "and" in name.lower():
        return  True
    return  False
result=df[df["player_name"].apply(str_find)]
print(result)