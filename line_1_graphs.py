
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


# In[4]:


#Calculate the Suicides per 100,000 People:
vet_per_cap_suic_per_year_list = []
for year in np.arange(2005,2012,1):
       vet_per_cap_suic_per_year_list.append(((veterans_df[f"vet_suicides_{year}"].sum())/(veterans_df[f"vet_pop_{year}"].sum()))*100000)

gen_pop_suic_per_year_list = []
for year in np.arange(2005,2012,1):
       gen_pop_suic_per_year_list.append(((veterans_df[f"all_suicides_{year}"].sum()-veterans_df[f"vet_suicides_{year}"].sum())/(veterans_df[f"overall_pop_18_{year}"].sum()-veterans_df[f"vet_pop_{year}"].sum()))*100000)


# In[5]:


#Graph the Suicide Rates:
sns.set()
x = np.arange(2005, 2012, 1) 
plt.plot(x, vet_per_cap_suic_per_year_list, label="Veteran Suicides", color='red', markersize=2, linewidth=2, marker='o')
plt.plot(x, gen_pop_suic_per_year_list, label="Non-Vet Suicides", color='blue', markersize=2, linewidth=2, marker='o')

plt.xlabel("Years 2005 - 2011")
plt.ylabel("Suicides per 100,000")
plt.title("Veteran Vs Non-Veteran Suicide Rates 2005-2011")
plt.legend()
plt.show()


# In[6]:


#Calculate the Suicides per 100,000 People:


# In[7]:


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


plt.title("Veteran and Overall Populations")
plt.xlabel("Years")
plt.ylabel("Populations in Hundred Millions")
plt.bar(x, y1, .5, label="Veterans", align='edge')
plt.bar(x+.5, y2, .5, label="Non-Vetrans", align="edge")
plt.legend(loc='upper left')
plt.ylim(0,300000000)
plt.show()

plt.title("Suicides by Year")
plt.xlabel("Years")
plt.ylabel("Suicides")
plt.bar(x, y3,  .5, label="Veterans")
plt.bar(x+.5, y4, .5, label="Non-Veterans")
plt.legend(loc='upper left')
plt.ylim(0, 50000)
plt.show()

