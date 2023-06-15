#Pomoću Pandas biblioteke učitajte covid-data.csv podatke i nađite kada je u Njemačkoj
#zabilježen prvi covid19 slučaj.
import pandas as pd
covid=pd.read_csv("covid-data.csv")
covid_njemčka=covid[(covid["location"] =="Germany")]
covid_njemčka=covid_njemčka.sort_values("date")

print(covid_njemčka)














