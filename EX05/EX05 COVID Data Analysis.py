#Author: Ashutosh Laxminarayan Gor

import csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('covid_comorbidities_USsummary.csv')
# print(df)
df_nocovid = df.drop(df[df['Condition'] == 'COVID-19'].index)

below35 = df_nocovid[(df_nocovid['Age Group'] == '0-24') | (df_nocovid['Age Group'] == '25-34')]

total_deaths = below35.groupby(['Condition']).sum().sort_values('COVID-19 Deaths', ascending = False).reset_index()

highest_deaths = total_deaths['COVID-19 Deaths'][0]

highest_deaths_condition = total_deaths['Condition'][0]

print('\n The comorbidity of highest number of deaths below age 35 is',highest_deaths_condition,'with', highest_deaths, 'deaths.')

age_group_deaths = df_nocovid.groupby(['Age Group']).sum()

age_group_deaths = age_group_deaths[age_group_deaths.index != 'All Ages']
age_group_deaths = age_group_deaths[age_group_deaths.index != 'Not stated']
print('\n Total count of people per class of age')
print('\n', age_group_deaths)

agegroup = list(age_group_deaths.index)
deaths = list(age_group_deaths['COVID-19 Deaths'])

a = plt.figure(figsize= (16,11))
a.suptitle('COVID-19 Comorbidity Death Count according to age group', fontsize=28)
ax = a.add_subplot(1,2,1)
ax.bar(agegroup,deaths)
ax.set_xlabel('Age Group', fontsize=16)
ax.set_ylabel('Deaths', fontsize=16)

agegroup_pie = [agegroup[0],agegroup[1],agegroup[2],agegroup[3],agegroup[4],agegroup[5],agegroup[6],agegroup[7]]
deaths_pie = [deaths[0],deaths[1],deaths[2],deaths[3],deaths[4],deaths[5],deaths[6],deaths[7]]

ax2 = a.add_subplot(1,2,2)
# ax2.pie(deaths_pie, labels = agegroup_pie, autopct= '%.1a%%', pctdistance = 0.8, labeldistance = 1.1)
ax2.pie(deaths_pie, labels = agegroup_pie, labeldistance = 1.1)
ax2.legend(loc='lower right', labels = agegroup_pie, title = 'Age Group')
plt.show()

print('\n run by Ashutosh Laxminarayan Gor')