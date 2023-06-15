#Stvorite DataFrame objekt koji predstavlja sljedeću strukturu podataka:
import pandas as pd


df=pd.DataFrame({"Model":["BMW 5","Mercedes A-class","Audi A8"],
                 "Godina": [2017,2020,2016],
                 "Kilometri":[50000,5000,30000]})




tip_motora_series=pd.Series(["Dizel","Beznin","Dizel"])

df=df.assign(tip_motora=tip_motora_series)
df.rename(columns={"tip_motora":"Tip motora"},inplace=True)

print(df)












