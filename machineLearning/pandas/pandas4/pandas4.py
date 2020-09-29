#Data Frame ile groupby kullanımı

import pandas as pd
import numpy as np
personeller={
    'Çalışan':['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman':['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş':[30,25,45,50,23,34,42],
    'Semt':['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş':[5000,3000,4000,3500,2750,6500,4500]
}
df=pd.DataFrame(personeller)
result=df
# result=df["Maaş"].sum()  # Maaşların toplamını verir
result=df.groupby("Departman").groups
result=df.groupby(["Departman","Semt"]).groups

# for name,group in df.groupby(["Departman" or "Semt"]):
#     print(name)
#     print(group) #Departman ve semte göre sıraladık

result=df.groupby("Semt").get_group("Kadıköy") #Semte göre seçtik
result=df.groupby("Departman").get_group("Muhasebe") #Departmana göre seçtik
result=df.groupby("Departman").sum() #Yaşların ve Maaşların toplamını getirir
result=df.groupby("Departman").mean() #Yaşların ve Maaşların ortalamasını getirir
result=df.groupby("Departman")["Maaş"].mean()  # Maaş ortalamasını hesaplandırır
result=df.groupby("Semt")["Yaş"].mean() #Semtlere göre yaş ortalaması
result=df.groupby("Semt")["Maaş"].mean() #Semtlere göre maaş ortalaması
result=df.groupby("Semt")["Çalışan"].count #Semtlere göre çalışan bilgisi verir
result=df.groupby("Departman")["Yaş"].max() #En çok kaç yasında olduğunu gösterir
result=df.groupby("Departman")["Yaş"].min() #En az kaç yasında olduğunu gösterir
result=df.groupby("Departman")["Maaş"].max() #En çok maaşı olduğunu gösterir
result=df.groupby("Departman")["Maaş"].min () #En az maaşı olduğunu gösterir
result=df.groupby("Departman")["Maaş"].max()["Muhasebe"] #En çok muhasebe maaşı olduğunu gösterir
result=df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]) #Birden fazla matematik argümanını getirir
result=df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"] #Bu bilgileri sadece muhasebeye göre getirir
print(result)

