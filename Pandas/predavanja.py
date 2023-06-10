import pandas as pd
import matplotlib.pyplot as plt
"""
my_dict={"Ime": ["Ana","Ivan","Marko"],
         "Godine":[18,20,22],
         "Spol":["Z","M","M"]}


df=pd.DataFrame(my_dict)

#print(df)

#imena=df["Ime"]
#print(imena)

radni_staz_series=pd.Series([1,3,5],name="Radni staz")
df=df.assign(radni_staz=radni_staz_series)
df.rename(columns={"radni_staz":"Radni staz"},inplace=True)
print(df)
"""
#oscars_df=pd.read_csv("oscar_age_male.csv")
#print(oscars_df.info())

#age_and_names=oscars_df[["Age","Name"]]
#print(age_and_names)

#older_than_40=oscars_df[oscars_df["Age"]>40]
#print(older_than_40)


#oscars_50_or_60_age=oscars_df.loc[(oscars_df["Age"]==50) | (oscars_df["Age"]==60),"Name"]
#print(oscars_50_or_60_age)

#oscars_50_or_60_age=oscars_df.iloc[2:5,1:3]
#print(oscars_50_or_60_age)

#oscars_df=oscars_df.sort_values(by="Age")
#print(oscars_df)

#oscars_df.plot(x="Year",y="Age")
#plt.show()

""""""""""""""""""

salaries_df=pd.read_csv("Salary_Data.csv")

age_bachelor=salaries_df.loc[salaries_df["Education Level"]=="Bachelor's","Age"]
experience_bachelor=salaries_df.loc[salaries_df["Education Level"]=="Bachelor's","Years of Experience"]
salaries_bachelor=salaries_df.loc[salaries_df["Education Level"]=="Bachelor's","Salary"]


age_master=salaries_df.loc[salaries_df["Education Level"]=="Master's","Age"]
experience_master=salaries_df.loc[salaries_df["Education Level"]=="Master's","Years of Experience"]
salaries_master=salaries_df.loc[salaries_df["Education Level"]=="Master's","Salary"]

age_phd=salaries_df.loc[salaries_df["Education Level"]=="PhD","Age"]
experience_phd=salaries_df.loc[salaries_df["Education Level"]=="PhD","Years of Experience"]
salaries_phd=salaries_df.loc[salaries_df["Education Level"]=="PhD","Salary"]



fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(age_bachelor,experience_bachelor,salaries_bachelor,c='red',marker='x',label='Bachelot\'s')
ax.scatter(age_master,experience_master,salaries_master,c='blue',marker='o',label='Master\'s')
ax.scatter(age_phd,experience_phd,salaries_phd,c='green',marker='o',label='PhD')
ax.set_xlabel("Age")
ax.set_ylabel("Experience")
ax.set_zlabel("Salarys")
ax.legend()
plt.show()
