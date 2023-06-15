#Kojeg datuma je zabilježeno najviše novih slučajeva u Hrvatskoj?
#Prikažite krivulju dnevnih zabilježenih covd19 slučajeva u Hrvatskoj iz covid-data.csv podataka.
import pandas as pd
import matplotlib.pyplot as plt

covid=pd.read_csv("covid-data.csv")
covid_hrvatska=covid[(covid["location"] =="Croatia")]
covid_hrvatska.plot(x="date",y="new_cases")
covid_hrvatska_najvise_u_danu=covid_hrvatska["new_cases"].max()
covid_hrvatska_najvise=covid_hrvatska.loc[covid_hrvatska["new_cases"]==covid_hrvatska_najvise_u_danu,"date"]
print(covid_hrvatska_najvise)
#plt.show()




