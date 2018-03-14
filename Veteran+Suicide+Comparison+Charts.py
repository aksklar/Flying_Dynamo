
# coding: utf-8

# In[1]:


# 1.	Average Suicidal Rate among Veterans vs Overall Population: 


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[3]:


veterans_df = pd.read_csv("veteran_suicides_2005-2011.csv")
veterans_df.head()


# In[4]:


#Calculate the Suicides per 100,000 People:
vet_per_cap_suic_per_year_list = []
for year in np.arange(2005,2012,1):
       vet_per_cap_suic_per_year_list.append(((veterans_df[f"vet_suicides_{year}"].sum())/(veterans_df[f"vet_pop_{year}"].sum()))*100000)

non_vet_suic_per_year_list = []
for year in np.arange(2005,2012,1):
       non_vet_suic_per_year_list.append(((veterans_df[f"all_suicides_{year}"].sum()-veterans_df[f"vet_suicides_{year}"].sum())/(veterans_df[f"overall_pop_18_{year}"].sum()-veterans_df[f"vet_pop_{year}"].sum()))*100000)

gen_pop_suic_per_year_list = []
for year in np.arange(2005,2012,1):
       gen_pop_suic_per_year_list.append(((veterans_df[f"all_suicides_{year}"].sum())/(veterans_df[f"overall_pop_18_{year}"].sum()))*100000)


# In[5]:


#Graph the Suicide Rates:
sns.set()
x = np.arange(2005, 2012, 1) 
plt.figure(figsize=(19,4))

plt.bar(x-.3, vet_per_cap_suic_per_year_list, label="Veteran Suicides", width=.3, color='steelblue')
plt.bar(x, gen_pop_suic_per_year_list, label="Overall Suicides",width=.3, color='mediumseagreen')
plt.bar(x+.3, non_vet_suic_per_year_list, label="Non-Vet Suicides",width=.3, color='dimgrey')

plt.xlabel("Years 2005 - 2011")
plt.ylabel("Suicides per 100,000")
plt.title("Veteran Vs Non-Veteran Suicide Rates 2005-2011")
plt.legend()
plt.xlim(2004, 2012)
plt.ylim(0, 45)
plt.show()


# In[6]:


#Calculate the Suicides Rates per 100,000 People:
x = np.arange(2005,2012,1)
y1 = []
y2 = []
y3 = []
y4 = []

for year in np.arange(2005,2012,1):
    y1.append(veterans_df[f"vet_pop_{year}"].sum())
    y2.append(veterans_df[f"overall_pop_18_{year}"].sum()-veterans_df[f"vet_pop_{year}"].sum())
    y3.append(veterans_df[f"vet_suicides_{year}"].sum())
    y4.append(veterans_df[f"all_suicides_{year}"].sum()-veterans_df[f"vet_suicides_{year}"].sum())

plt.figure(figsize=(5,5))
plt.title("Average Veteran VS Non-Veteran Suicide Rate 2005-2011 ")
plt.pie(
    [np.mean(vet_per_cap_suic_per_year_list),np.mean(non_vet_suic_per_year_list)],
    explode=[.1,0],
    labels=["Veterans", "Non Veterans"],
    autopct='%.2f',
    pctdistance=.6
    #colors=['red', 'blue']
)
    
plt.axis("equal")
plt.show()


# In[7]:


#What percentage of suicides come from veterans:
total_vet_suicides_list = []
total_non_vet_suicides_list = []
for year in np.arange(2005,2012,1):
    total_vet_suicides_list.append(veterans_df[f"vet_suicides_{year}"].sum())
    total_non_vet_suicides_list.append(veterans_df[f"all_suicides_{year}"].sum()-veterans_df[f"vet_suicides_{year}"].sum())
total_vet_suicides = np.sum(total_vet_suicides_list)
total_non_vet_suicides = np.sum(total_non_vet_suicides_list)

plt.figure(figsize=(5,5))
plt.title("Percentage of Suicides that Come from Veterans")
plt.pie(
    [total_vet_suicides, total_non_vet_suicides],
    explode=[.1,0],
    labels=["Veterans", "Non Veterans"],
    autopct='%.2f',
    pctdistance=.6
)
plt.axis('equal')
plt.show()


# In[13]:


#Daily Average of Veteran Suicides
sns.set()
x = np.arange(2005, 2012, 1) 
plt.figure(figsize=(19,4))

plt.bar(x-.3, np.divide(total_vet_suicides_list, 365), label="Veteran Suicides", width=.3, color='steelblue')
plt.bar(x, (np.divide(total_non_vet_suicides_list, 365)) , label="Non-Vet Suicides",width=.3, color='mediumseagreen')
#plt.bar(x+.3, non_vet_suic_per_year_list, label="Non-Vet Suicides",width=.3, color='dimgrey')

plt.xlabel("Years 2005 - 2011")
plt.ylabel("Daily Average of Suicides")
plt.title("Daily Average of Suicides Per Year, 2005-2011")
plt.legend()
plt.xlim(2004, 2012)
plt.ylim(0, 100)
plt.show()

