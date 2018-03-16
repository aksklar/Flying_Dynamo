
# coding: utf-8

# In[64]:


import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[65]:


# Read and create dataframe for female vets
female_csvpath = "veteran_data/Vet Suicides 2005-2014 (Females).csv"
female_vets_df = pd.read_csv(female_csvpath)
female_vets_df = female_vets_df.set_index("female")
female_vets_df


# In[66]:


# Read and create dataframe for male vets
male_csvpath = "veteran_data/Vet Suicides 2005-2014 (Males).csv"
male_vets_df = pd.read_csv(male_csvpath)
male_vets_df = male_vets_df.set_index("male")
male_vets_df


# In[98]:


# Calculate averages for female vets
female_avgs = []
for column in female_vets_df:
    avgs = (female_vets_df[column]).mean()
    female_avgs.append(avgs)
# Calculate averages for male vets
male_avgs = []
for column in male_vets_df:
    avgs = (male_vets_df[column]).mean()
    male_avgs.append(avgs)


# In[99]:


# Combine averages into a list for plotting
avgs_list = [male_avgs, female_avgs]
total_list = [male + female for male, female in zip(male_avgs, female_avgs)]
total_avg_list = [x / 2 for x in total_list]
years_list = ["2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]
# Give chart title, labels, and ticks
sns.set_style("darkgrid")
plt.title("Average Vet Suicide Rate by Gender (2005-2014)")
plt.xlabel("Year")
plt.ylabel("Average Rate of Suicide (%)")
plt.xticks(np.arange(11), years_list)
# Plotting bar chart
x = np.arange(10)
plt.bar(x + 0.00, total_avg_list, color= 'seagreen', width = 0.25, label="Total")
plt.bar(x + 0.25, avgs_list[0], color = 'deepskyblue', width = 0.25, label="Males")
plt.bar(x + 0.50, avgs_list[1], color = 'coral', width = 0.25, label="Females")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.6))
plt.show()


# In[100]:


# Give chart titles, labels, and limits
plt.title("Average Vet Suicides Rate by Gender (2005-2014)")
plt.xlabel("Year")
plt.ylabel("Yearly Average Rate of Suicide (%)")
#plt.xlim(2005, 2014)
plt.ylim(5, 50)
# Create handles for legend and plot line graph with grid
Female, = plt.plot(years_list, female_avgs, marker="o", color="coral", label="Females")
Male, = plt.plot(years_list, male_avgs, marker="s", color="deepskyblue", label="Males")
plt.legend(handles=[Female, Male], loc='center left', bbox_to_anchor=(1, 0.6))
plt.show()

