#Grafički prikažite krivulju novozaraženih nakon što je u Hrvatskoj počelo cijepljenje (koristite
#podatke iz people_fully_vaccinated kolone).Graf treba prikazivati ovisnost novozaraženih u
#odnosu na ukupan broj cijepljenih.
import pandas as pd
import matplotlib.pyplot as plt

covid=pd.read_csv("covid-data.csv")
covid_hrvatska=covid[(covid["location"] =="Croatia")]

covid_hrvatska.plot(x="people_fully_vaccinated",y="new_cases")
plt.show()



















