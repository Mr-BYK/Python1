import numpy as np
import pandas as pd
#Pandas ile String Fonksiyonları
# data=pd.read_csv("nba.csv")
#NaN değerleri kaldırıyoruz
# data.dropna(inplace=True)
#Data sütunlarını görüyoruz
# print(data.columns)
#Bütün isimleri büyük harf yaptık
# data["player_name"]=data["player_name"].str.upper()
# Find parametresini kullanarak arama işlemi yapıyoruz
# data["index"]=data["player_name"].str.find("a")
#Jordan ismi geçen bütün kayıtları aratıyoruz
# data=data[data.player_name.str.contains("Jordan")]
# print(data)


#//////////////////////////////////////////////////////////////////////

# customers={
#     "CustomerId":[1,2,3,4],
#     "FirstName":["Ahmet","Ali","Hasan","Canan"],
#     "Lastname":["Yılmaz","Korkmaz","Çelik","Toprak"]
# }
#
# orders={
#     "OrderId":[10,11,12,13],
#     "CustomerId":[1,2,5,7],
#     "OrderDate":["2017-07-07","2017-08-07","2017-09-07","2020-10-07"]
# }
# df_customers=pd.DataFrame(customers,columns=["CustomerId","FirstName","Lastname"])
# df_orders=pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])
#
# print(df_orders)
# print(df_customers)
# Şiparişi alınan müşretileri getirdik
# result=pd.merge(df_customers,df_orders,how="inner")
# Bütün müşterileri getirdik
# result=pd.merge(df_customers,df_orders,how="left")
# result=pd.merge(df_customers,df_orders,how="outer")
# print(result)

# customersA={
#     "CustomerId":[1,2,3,4],
#     "FirstName":["Ahmet","Ali","Hasan","Canan"],
#     "Lastname":["Yılmaz","Korkmaz","Çelik","Toprak"]
# }
# customersB={
#     "CustomerId":[4,5,6,7],
#     "FirstName":["Yasin","Sinem","Hasan","Can"],
#     "Lastname":["Bilge","Ardıç","Çaktı","Duran"]
# }
# df_customersA=pd.DataFrame(customersA,columns=["CustomerId","FirstName","Lastname"])
# df_customersB=pd.DataFrame(customersB,columns=["CustomerId","FirstName","Lastname"])
# # Bütün kullanıcıları birleştirdik
# # result=pd.concat([df_customersA,df_customersB]) #Sütuna göre
# result=pd.concat([df_customersA,df_customersB],axis=1) #Satıra göre
# print(result)



# ////////////////////////////////////////////////////////////////////////////////
# Pandas DataFrame Metotları
data={
    "Column1":[1,2,3,4,5],
    "Column2":[10,20,13,45,25],
    "Column3":["abc","cba","ade","bca","dea"]
}
df=pd.DataFrame(data)
result=df
# Column2 Tekrarlanmadan verileri getirir
result=df["Column2"].unique()
# Column2 kaç tane veri olduğunu  getirir
result=df["Column2"].nunique()
# Column2 Her bir elemanın kaç kere tekrarlandığını getirir
result=df["Column2"].value_counts()
# Column2 karesini aldırır
result=df["Column2"]*2

def kareal(x):
    return x*x
# Column2 nin karesini alır
result=df["Column2"].apply(kareal),
# Sütun sayısının toplamını verir
result=len(df.columns)
print(result)