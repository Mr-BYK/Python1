import pandas as pd

"""
Basit düzeyde dataframe  yapısı oluşturma
s1=pd.Series([3,2,0,1])
s2=pd.Series([0,3,7,2])
data=dict(apples=s1 , oranges=s2)
df=pd.DataFrame(data)
print(df)
"""

"""
df=pd.DataFrame()
df=pd.DataFrame([1,2,3,4])
df=pd.DataFrame([["Ahmed,80"],["Yusuf,90"],["Basir,70"],["Mohammed,100"]])
dict={"Name":["Ahmed","Yusuf","Basir","Mohammed"],"Grade":[50,60,70,80]}
dict_list=[
            {"Name":"Ahmet","Grade":80},
            {"Name":"Yusuf","Grade":90},
            {"Name":"Basir","Grade":70},
            {"Name":"Mohammed","Grade":100}
      ]
df=pd.DataFrame(dict)
df=pd.DataFrame(dict,index=["212","232","236","456"])
print(df)
"""
