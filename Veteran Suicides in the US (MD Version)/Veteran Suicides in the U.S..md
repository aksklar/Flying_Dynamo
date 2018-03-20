

```python
import csv
import pandas as pd
import numpy as np
import scipy.stats as st
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import interactive
import plotly
import plotly.plotly as py
from plotly.offline import init_notebook_mode
import plotly.graph_objs as go
init_notebook_mode(connected=True)
```


<script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window.Plotly) {{require(['plotly'],function(plotly) {window.Plotly=plotly;});}}</script>



```python
# Loop through raw CSVs to add years in column header
years = [2005, 2006, 2007, 2008, 2009, 2010, 2011]
for year in years:
    
    #Append each needed column's name with the year:
    csv_df = pd.read_csv(f"veteran_data/us-veteran-suicides-raw/{year}.csv")
    
    for x in np.arange(2,8,1):
        csv_df.columns.values[x] = csv_df.columns.values[x] + f"_{year}"
        
    csv_df.to_csv(f"veteran_data/{year}.csv")
```


```python
# Read CSVs
csv2005_df = pd.read_csv("veteran_data/2005.csv", index_col=0)
csv2006_df = pd.read_csv("veteran_data/2006.csv", index_col=0)
csv2007_df = pd.read_csv("veteran_data/2007.csv", index_col=0)
csv2008_df = pd.read_csv("veteran_data/2008.csv", index_col=0)
csv2009_df = pd.read_csv("veteran_data/2009.csv", index_col=0)
csv2010_df = pd.read_csv("veteran_data/2010.csv", index_col=0)
csv2011_df = pd.read_csv("veteran_data/2011.csv", index_col=0)
```


```python
# Clean CSVs by dropping columns with missing information
cleaned2005 = csv2005_df.drop(columns=['vet_males', 'vet_males_p','vet_females','vet_females_p','vet_15_24','vet_18_29','vet_17_34','vet_25_34','vet_30_39','vet_25_44','vet_35_44','vet_40_49','vet_35-54','vet_45_54','vet_50_59','vet_45_64','vet_55_64','vet_60','vet_65','vet_rate','civ_rate'])
cleaned2006 = csv2006_df.drop(columns=['vet_males','vet_males_p','vet_females','vet_females_p','vet_15_24','vet_18_29','vet_17_34','vet_25_34','vet_30_39','vet_25_44','vet_35_44','vet_40_49','vet_35-54','vet_45_54','vet_50_59','vet_45_64','vet_55_64','vet_60','vet_65','vet_rate','civ_rate'])
cleaned2007 = csv2007_df.drop(columns=['vet_males','vet_males_p','vet_females','vet_females_p','vet_15_24','vet_18_29','vet_17_34','vet_25_34','vet_30_39','vet_25_44','vet_35_44','vet_40_49','vet_35-54','vet_45_54','vet_50_59','vet_45_64','vet_55_64','vet_60','vet_65','vet_rate','civ_rate'])
cleaned2008 = csv2008_df.drop(columns=['vet_males','vet_males_p','vet_females','vet_females_p','vet_15_24','vet_18_29','vet_17_34','vet_25_34','vet_30_39','vet_25_44','vet_35_44','vet_40_49','vet_35-54','vet_45_54','vet_50_59','vet_45_64','vet_55_64','vet_60','vet_65','vet_rate','civ_rate'])
cleaned2009 = csv2009_df.drop(columns=['vet_males','vet_males_p','vet_females','vet_females_p','vet_15_24','vet_18_29','vet_17_34','vet_25_34','vet_30_39','vet_25_44','vet_35_44','vet_40_49','vet_35-54','vet_45_54','vet_50_59','vet_45_64','vet_55_64','vet_60','vet_65','vet_rate','civ_rate'])
cleaned2010 = csv2010_df.drop(columns=['vet_males','vet_males_p','vet_females','vet_females_p','vet_15_24','vet_18_29','vet_17_34','vet_25_34','vet_30_39','vet_25_44','vet_35_44','vet_40_49','vet_35-54','vet_45_54','vet_50_59','vet_45_64','vet_55_64','vet_60','vet_65','vet_rate','civ_rate'])
cleaned2011 = csv2011_df.drop(columns=['vet_males','vet_males_p','vet_females','vet_females_p','vet_15_24','vet_18_29','vet_17_34','vet_25_34','vet_30_39','vet_25_44','vet_35_44','vet_40_49','vet_35-54','vet_45_54','vet_50_59','vet_45_64','vet_55_64','vet_60','vet_65','vet_rate','civ_rate'])
```


```python
cleaned2005 = cleaned2005.drop(cleaned2005.columns[0], axis=1)
cleaned2006 = cleaned2006.drop(cleaned2006.columns[0], axis=1)
cleaned2007 = cleaned2007.drop(cleaned2007.columns[0], axis=1)
cleaned2008 = cleaned2008.drop(cleaned2008.columns[0], axis=1)
cleaned2009 = cleaned2009.drop(cleaned2009.columns[0], axis=1)
cleaned2010 = cleaned2010.drop(cleaned2010.columns[0], axis=1)
cleaned2011 = cleaned2011.drop(cleaned2011.columns[0], axis=1)
```


```python
to_be_merged = ['cleaned2005', 'cleaned2006', 'cleaned2007', 'cleaned2008', 'cleaned2009', 'cleaned2010', 'cleaned2011']
```


```python
# Merge CSVs to create new CSV
merged = pd.merge(cleaned2005, cleaned2006, how='outer', on='state')
merged = pd.merge(merged, cleaned2007, how='outer', on='state')
merged = pd.merge(merged, cleaned2008, how='outer', on='state')
merged = pd.merge(merged, cleaned2009, how='outer', on='state')
merged = pd.merge(merged, cleaned2010, how='outer', on='state')
merged = pd.merge(merged, cleaned2011, how='outer', on='state')
merged.to_csv('veteran_data/veteran_suicides_2005-2011.csv')
```

## Veteran Suicides in the United States (2005 - 2011)
Over the years, veterans consistently commit suicide at a much higher rate than the overall population.  Here we see that veterans take their own lives at about double the rate than non-veterans.  From 2005 to 2011, almost a fifth of all suicides in the United States were veterans.  The problem is increasing, as the average rate of suicide for veterans has increased from around eighteen per day to over twenty per day. 


```python
# Open new CSV
veterans_df = pd.read_csv("veteran_data/veteran_suicides_2005-2011.csv")
veterans_df = veterans_df.drop(columns='Unnamed: 0')
veterans_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>state</th>
      <th>vet_pop_2005</th>
      <th>overall_pop_18_2005</th>
      <th>vet_pop_p_2005</th>
      <th>vet_suicides_2005</th>
      <th>all_suicides_2005</th>
      <th>vet_suicides_p_2005</th>
      <th>vet_pop_2006</th>
      <th>overall_pop_18_2006</th>
      <th>vet_pop_p_2006</th>
      <th>...</th>
      <th>vet_pop_p_2010</th>
      <th>vet_suicides_2010</th>
      <th>all_suicides_2010</th>
      <th>vet_suicides_p_2010</th>
      <th>vet_pop_2011</th>
      <th>overall_pop_18_2011</th>
      <th>vet_pop_p_2011</th>
      <th>vet_suicides_2011</th>
      <th>all_suicides_2011</th>
      <th>vet_suicides_p_2011</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alabama</td>
      <td>403950</td>
      <td>3344721</td>
      <td>0.120772</td>
      <td>135</td>
      <td>535</td>
      <td>0.252336</td>
      <td>408917</td>
      <td>3473558</td>
      <td>0.117723</td>
      <td>...</td>
      <td>0.110360</td>
      <td>156</td>
      <td>679</td>
      <td>0.229750</td>
      <td>395753</td>
      <td>3662910</td>
      <td>0.108043</td>
      <td>163</td>
      <td>680</td>
      <td>0.239706</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alaska</td>
      <td>74482</td>
      <td>446969</td>
      <td>0.166638</td>
      <td>24</td>
      <td>131</td>
      <td>0.183206</td>
      <td>70067</td>
      <td>478581</td>
      <td>0.146406</td>
      <td>...</td>
      <td>0.140705</td>
      <td>35</td>
      <td>164</td>
      <td>0.213415</td>
      <td>72407</td>
      <td>517799</td>
      <td>0.139836</td>
      <td>27</td>
      <td>142</td>
      <td>0.190141</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Arizona</td>
      <td>538880</td>
      <td>4238996</td>
      <td>0.127124</td>
      <td>225</td>
      <td>945</td>
      <td>0.238095</td>
      <td>558906</td>
      <td>4521911</td>
      <td>0.123600</td>
      <td>...</td>
      <td>0.111217</td>
      <td>240</td>
      <td>1093</td>
      <td>0.219579</td>
      <td>533608</td>
      <td>4842927</td>
      <td>0.110183</td>
      <td>242</td>
      <td>1091</td>
      <td>0.221815</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Arkansas</td>
      <td>259304</td>
      <td>2023819</td>
      <td>0.128126</td>
      <td>81</td>
      <td>400</td>
      <td>0.202500</td>
      <td>258170</td>
      <td>2110583</td>
      <td>0.122322</td>
      <td>...</td>
      <td>0.112340</td>
      <td>105</td>
      <td>447</td>
      <td>0.234899</td>
      <td>238790</td>
      <td>2221409</td>
      <td>0.107495</td>
      <td>89</td>
      <td>447</td>
      <td>0.199105</td>
    </tr>
    <tr>
      <th>4</th>
      <td>California</td>
      <td>2193336</td>
      <td>25543447</td>
      <td>0.085867</td>
      <td>633</td>
      <td>3206</td>
      <td>0.197442</td>
      <td>2142367</td>
      <td>26789221</td>
      <td>0.079971</td>
      <td>...</td>
      <td>0.069784</td>
      <td>705</td>
      <td>3913</td>
      <td>0.180169</td>
      <td>1910994</td>
      <td>28292703</td>
      <td>0.067544</td>
      <td>706</td>
      <td>3923</td>
      <td>0.179964</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 43 columns</p>
</div>




```python
#Calculate the Suicides per 100,000 People
vet_per_cap_suic_per_year_list = []
for year in np.arange(2005,2012,1):
       vet_per_cap_suic_per_year_list.append(((veterans_df[f"vet_suicides_{year}"].sum())
                                              /(veterans_df[f"vet_pop_{year}"].sum()))*100000)

non_vet_suic_per_year_list = []
for year in np.arange(2005,2012,1):
       non_vet_suic_per_year_list.append(((veterans_df[f"all_suicides_{year}"].sum()
                                           -veterans_df[f"vet_suicides_{year}"].sum())
                                          /(veterans_df[f"overall_pop_18_{year}"].sum()
                                            -veterans_df[f"vet_pop_{year}"].sum()))*100000)

gen_pop_suic_per_year_list = []
for year in np.arange(2005,2012,1):
       gen_pop_suic_per_year_list.append(((veterans_df[f"all_suicides_{year}"].sum())
                                          /(veterans_df[f"overall_pop_18_{year}"].sum()))*100000)
```


```python
#Graph the Suicide Rates
sns.set(style="whitegrid")
x = np.arange(2005, 2012, 1) 
plt.figure(figsize=(19,4))

plt.bar(x-.3, vet_per_cap_suic_per_year_list, label="Veteran Suicides", width=.3, color='steelblue')
plt.bar(x, gen_pop_suic_per_year_list, label="Overall Suicides",width=.3, color='mediumseagreen')
plt.bar(x+.3, non_vet_suic_per_year_list, label="Non-Vet Suicides",width=.3, color='dimgrey')

plt.xlabel("Year")
plt.ylabel("Suicides per 100,000")
plt.title("Veteran Vs Non-Veteran Average Suicide Rates 2005-2011")
plt.legend()
plt.ylim(0, 45)
plt.savefig("Vet_vs_Non-Vet_Suicide_Rates")
plt.show()
```


![png](output_10_0.png)



```python
# Calculate the Suicides Rates per 100,000 People:
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
    pctdistance=.6)
    # colors=['red', 'blue']
plt.axis("equal")
plt.savefig("Avg_Suicide_Vet_vs_NonVet")
plt.show()
```


![png](output_11_0.png)



```python
# What percentage of suicides come from veterans
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
    pctdistance=.6)
plt.axis('equal')
plt.savefig("Percent_of_Vet_Suicides")
plt.show()
```


![png](output_12_0.png)



```python
# Average veteran suicides per day
sns.set(style="whitegrid")
x = np.arange(2005, 2012, 1)
plt.figure(figsize=(10,4))
plt.title("Average Veteran Suicides Per Day")
plt.xlabel("Year")
plt.ylabel("Average Veteran Suicides Per Day")
plt.plot(x-.3, np.divide(total_vet_suicides_list, 365), label="Average Veteran Suicides Per Day", color='steelblue')
plt.savefig("Avg_Daily_Vet_Suicides")
plt.show()
```


![png](output_13_0.png)


## Veteran Suicides by State (2005 - 2011)
The suicide rates by state shows Montana, Idaho, Nevada, and New Mexico had the highest rates of veteran suicides, in which the four states are averaging at the rate of 50.49 suicides per 100,000 people.  In further analysis, we found that the states with the highest suicide rates also had very few VHA centers in their respective states.


```python
# Read CSVs
state_df = pd.read_csv("veteran_data/50_usstates_data.csv")
vha_df = pd.read_csv("veteran_data/VHA_Center.csv", encoding="ISO-8859-1")
```


```python
# Group by state  
# Calculating the mean of vet suicides data for years 2005 to 2011 by state 
# Suicide rate calculation

vet_suicideratelist = []
nonvet_suicideratelist = []
statelist= []
vets_state = veterans_df.set_index('state')

for index,row in vets_state.iterrows():
    
    #Overall population from 2005 to 2011 satewise
    overallpop = (row[1] + row[7]+ row[13] + row[19] +row[25] + row[31] + row[37])
    vetpop = (row[0] + row[6] + row[12] + row[18] + row[24] + row[30] + row[36])
    nonvetpop = (overallpop - vetpop)
    
    overall_suicide = (row[4] + row[10]+ row[16]+ row[22]+row[28]+row[34]+row[40])
    vet_suicide = (row[3] + row[9]+ row[15]+ row[21]+row[27]+row[33]+row[39])
    nonvet_suicide = (overall_suicide - vet_suicide)
    
    vet_suiciderate = round((vet_suicide / vetpop) *100000, 2)
    nonvet_suiciderate = round((nonvet_suicide / nonvetpop) *100000,2)
    
    vet_suicideratelist.append(vet_suiciderate)
    nonvet_suicideratelist.append(nonvet_suiciderate)
    statelist.append(index)

# Turn list into to dataframe
suicide_state = pd.DataFrame({'statelist':statelist, 'vet_suicideratelist':vet_suicideratelist, 
                              'nonvet_suicideratelist' : nonvet_suicideratelist})

# Reorder columns 
suicide_state = suicide_state[['statelist', 'vet_suicideratelist','nonvet_suicideratelist']]

# Sort based on value 
vets_suicide_state = suicide_state.sort_values(by=['vet_suicideratelist'], ascending=False)
vets_suicide_state = vets_suicide_state.reset_index(drop=True)
#vets_suicide_state.head()
```


```python
# Graph plot state by state comparison of VETERAN suicide
fontsize = 15
sns.set(style="white")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 10))

# x position and y position data 
y_pos = vets_suicide_state['statelist']
x_pos = vets_suicide_state['vet_suicideratelist']

# Setting the colors
sns.set_color_codes("pastel")
# color = ["#DF0101", "#B40404", "#DF3A01", "#FF8000", "#FAAC58"]
sns.barplot(x_pos, y_pos,
            label="Total", palette="GnBu_d")

plt.xlim(0,60,5)

for i, v in enumerate(x_pos):
    plt.text(v + 2, i + .15, str(v), color='black', fontweight='bold', fontsize = 10)

# Add a legend and informative axis label
plt.title("Veteran Suicide Rate by States",fontsize = fontsize)
plt.xlabel("Veteran Suicide Rate", fontsize= fontsize)
plt.ylabel("States")
sns.despine(left=True, bottom=True)
plt.savefig("Veteran_Sucide_Rate")
plt.show()
```


![png](output_17_0.png)



```python
# Create new dataframe and sort values for non-vet suicides by state
nonvet_suicide_state = suicide_state[['statelist', 'nonvet_suicideratelist', 'vet_suicideratelist']]
nonvet_suicide_state = nonvet_suicide_state.sort_values(by=['nonvet_suicideratelist'], ascending=False)
```


```python
# Graph plot State by state comparison of Non VETERAN Suicide 
sns.set(style="white")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 10))

# x position and y position data 
y_pos = nonvet_suicide_state['statelist']
x_pos =nonvet_suicide_state['nonvet_suicideratelist']

# Setting the colors
sns.set_color_codes("pastel")
#color = ["#DF0101", "#B40404", "#DF3A01", "#FF8000", "#FAAC58"]
sns.barplot(x_pos, y_pos,
            label="Total", palette="GnBu_d")

plt.xlim(0,32,5)
for i, v in enumerate(x_pos):
    plt.text(v + 2, i + .15, str(v), color='black', fontweight='bold', fontsize = 8 )

# Add a legend and informative axis label
plt.title("Non-Veteran Suicide Rates State Comparison",fontsize = 15)
plt.xlabel("Non-Veteran Suicide Rate")
plt.ylabel("States")
sns.despine(left=True, bottom=True)
plt.savefig("Non_Veteran_Sucide_Rate")
plt.show()
```


![png](output_19_0.png)



```python
# Merge CSVs and group by VHA Centers
vha_state_merge = pd.merge(state_df, vha_df, how = "outer", on = "state abbreviation")
vhacount_df = vha_state_merge.groupby(["state"]).count()
vhacount_df = vhacount_df.reset_index()
vhacount_df.columns

# Create new dataframe with sorted vha centers
vhasort_df = vhacount_df.sort_values(by=["Facility"], ascending = False)
vhasort_df = vhasort_df.reset_index(drop=True)
```


```python
# Graph plot state by state comparison of VHA centers
fontsize = 15
sns.set(style="whitegrid")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 10))

# x position and y position data 
y_pos = vhasort_df['state']
x_pos =vhasort_df['Facility']

# Setting the colors
sns.set_color_codes("pastel")
# color = ["#DF0101", "#B40404", "#DF3A01", "#FF8000", "#FAAC58"]
sns.barplot(x_pos, y_pos,
            label="Total", palette="Reds")

plt.xlim(0,17,5)
for i, v in enumerate(x_pos):
    plt.text(v + .5, i , str(v), color='black', fontweight='bold', fontsize = 10)

# Add a legend and informative axis label
plt.title("VHA Centers by States",fontsize = fontsize)
plt.xlabel("VHA Center ", fontsize= fontsize)
plt.ylabel("States")
sns.despine(left=True, bottom=True)
plt.savefig("VHA_Centers_US")
plt.show()
```


![png](output_21_0.png)



```python
state_merge = pd.merge(veterans_df, vhacount_df, how = 'outer', on = 'state')
state_merge = state_merge.set_index('state')
state_merge.shape
```




    (50, 51)




```python
state_vet_suicide_list = []
state_vet_pop_list = []
state_list = []
state_c = []
vha_center_list = []

for index, row in state_merge.iterrows():
    total_pop = (row[1] + row[7] + row[13] + row[19] + row[25] + row[31] + row[37])
    vet_state_pop = (row[0] + row[6] + row[12] + row[18] + row[24] + row[30] + row[36])
    vet_state_suicide = (row[3] + row[9] + row[15] + row[21] + row[27] + row[33] + row[39])
    vet_suicide_rate = round((vet_state_suicide / vet_state_pop) *100000, 2)
    facilities = row[48]
    
    state_vet_pop_list.append(vet_state_pop)
    state_vet_suicide_list.append(vet_suicide_rate)
    state_list.append(index)
    vha_center_list.append(facilities)

state_by_state_df = pd.DataFrame({'State': state_list, 'Vet Suicide Rate': state_vet_suicide_list,
                                  'Vet Population': state_vet_pop_list, 'VHA Centers': vha_center_list, 
                                  'State Code': state_df['state abbreviation']})
state_by_state_df = state_by_state_df[['State Code', 'State', 'Vet Suicide Rate', 
                                       'Vet Population', 'VHA Centers']]
```


```python
for col in state_by_state_df.columns:
    state_by_state_df[col] = state_by_state_df[col].astype(str)

scl = [[0.0, 'rgb(204, 255, 102)'],[0.4, 'rgb(179, 255, 26)'],\
            [0.6, 'rgb(136, 204, 0)'],[0.8, 'rgb(85, 128, 0)'],[1.0, 'rgb(0, 128, 0)']]

state_by_state_df['text'] = state_by_state_df['State'] + ':' + state_by_state_df['State Code'] + '<br>' +\
'Veterans Population' + state_by_state_df['Vet Population'] + '<br>' +\
'Suicide Rate' + state_by_state_df['Vet Suicide Rate'] + '<br>' + 'VHA Count' + state_by_state_df['VHA Centers']
```


```python
state_data = [dict(
        type = 'choropleth',
        colorscale = scl,
        autocolorscale = False,
        locations = state_by_state_df['State Code'],
        z= state_by_state_df['Vet Suicide Rate'],
        locationmode = 'USA-states',
        text = state_by_state_df['text'],
        marker = dict(
            line = dict(
                color = 'rgb(51,51,51)',
                width = 2
            )),
        colorbar = dict(
                title = "Veteran Suicide <br>State Comparison",
                titleside = 'left',
                tickmode = 'array',
                tickvals = [55,35,15],
                ticktext = ['High','Medium','Less'],
                ticks = 'outside'
                )
            )]

layout = dict(
        title = 'Veteran Suicides State Comparison',
        geo = dict(
            scope = 'usa',
            projection=dict(type = 'albers usa'),
            showlakes = True,
            lakecolor = 'rgb(0, 138, 230)'),
            )
```


```python
fig = dict(data= state_data, layout = layout)
choromap = go.Figure(data = state_data, layout = layout)
plotly.offline.plot(choromap)
```




    'file://C:\\Users\\alain\\desktop\\Project One\\temp-plot.html'



## Veteran Suicides by Age Group
When analyzing the data by age group, there was a nineteen percent higher risk of suicides among veterans compared to
their civilian counterparts.  As a whole, older veterans make up for the majority of suicides; roughly sixty-nine percent were age fifty-five or older.


```python
# Read CSVs and create dataframe
vets_df = pd.read_csv("veteran_data/veteran_suicide_age_2005-2008.csv")
vets_age_df = vets_df
vets_age_df = vets_age_df.set_index('age_range')
vets_age_df.head(7)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>vet_suicide_2005</th>
      <th>vet_suicide_2006</th>
      <th>vet_suicide_2007</th>
      <th>vet_suicide_2008</th>
      <th>Nonvet_suicide_2005</th>
      <th>Nonvet_suicide_2006</th>
      <th>Nonvet_suicide_2007</th>
      <th>Nonvet_suicide_2008</th>
      <th>vet_pop_16sates</th>
      <th>v_rate_pop</th>
      <th>nonvet_pop_16sates</th>
      <th>nv_rate_pop</th>
    </tr>
    <tr>
      <th>age_range</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18-29</th>
      <td>12</td>
      <td>11</td>
      <td>23</td>
      <td>15</td>
      <td>86</td>
      <td>552</td>
      <td>759</td>
      <td>910</td>
      <td>65974</td>
      <td>0.201657</td>
      <td>4442150</td>
      <td>0.088096</td>
    </tr>
    <tr>
      <th>30-39</th>
      <td>71</td>
      <td>83</td>
      <td>92</td>
      <td>83</td>
      <td>865</td>
      <td>882</td>
      <td>861</td>
      <td>882</td>
      <td>302379</td>
      <td>0.150336</td>
      <td>4997418</td>
      <td>0.108549</td>
    </tr>
    <tr>
      <th>40-49</th>
      <td>183</td>
      <td>195</td>
      <td>185</td>
      <td>185</td>
      <td>1008</td>
      <td>994</td>
      <td>1049</td>
      <td>1017</td>
      <td>544281</td>
      <td>0.210210</td>
      <td>4804281</td>
      <td>0.111739</td>
    </tr>
    <tr>
      <th>50-59</th>
      <td>486</td>
      <td>453</td>
      <td>495</td>
      <td>487</td>
      <td>1092</td>
      <td>1012</td>
      <td>1062</td>
      <td>1083</td>
      <td>808175</td>
      <td>0.237569</td>
      <td>4852566</td>
      <td>0.114216</td>
    </tr>
    <tr>
      <th>60-69</th>
      <td>385</td>
      <td>450</td>
      <td>525</td>
      <td>553</td>
      <td>495</td>
      <td>321</td>
      <td>810</td>
      <td>615</td>
      <td>1412933</td>
      <td>0.077739</td>
      <td>2969481</td>
      <td>0.106765</td>
    </tr>
    <tr>
      <th>70-79</th>
      <td>494</td>
      <td>565</td>
      <td>485</td>
      <td>462</td>
      <td>427</td>
      <td>196</td>
      <td>216</td>
      <td>226</td>
      <td>1094061</td>
      <td>0.200000</td>
      <td>1424385</td>
      <td>0.102050</td>
    </tr>
    <tr>
      <th>80+</th>
      <td>808</td>
      <td>712</td>
      <td>595</td>
      <td>821</td>
      <td>97</td>
      <td>197</td>
      <td>148</td>
      <td>153</td>
      <td>1269990</td>
      <td>0.280000</td>
      <td>627695</td>
      <td>0.110654</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Calculating standard deviations for vets and non vets by age group
std_18_29 = st.stats.sem(vets_age_df.loc['18-29','vet_suicide_2005':'vet_suicide_2008'])/4
std_30_39 = st.stats.sem(vets_age_df.loc['30-39','vet_suicide_2005':'vet_suicide_2008'])/4
std_40_49 = st.stats.sem(vets_age_df.loc['40-49','vet_suicide_2005':'vet_suicide_2008'])/4
std_50_59 = st.stats.sem(vets_age_df.loc['50-59','vet_suicide_2005':'vet_suicide_2008'])/4
std_60_69 = st.stats.sem(vets_age_df.loc['60-69','vet_suicide_2005':'vet_suicide_2008'])/4
std_70_79 = st.stats.sem(vets_age_df.loc['70-79','vet_suicide_2005':'vet_suicide_2008'])/4
std_80 = st.stats.sem(vets_age_df.loc['80+','vet_suicide_2005':'vet_suicide_2008'])/4 

std_18_29_nonvet = st.stats.sem(vets_age_df.loc['18-29','Nonvet_suicide_2005':'Nonvet_suicide_2008'])/4
std_30_39_nonvet = st.stats.sem(vets_age_df.loc['30-39','Nonvet_suicide_2005':'Nonvet_suicide_2008'])/4
std_40_49_nonvet = st.stats.sem(vets_age_df.loc['40-49','Nonvet_suicide_2005':'Nonvet_suicide_2008'])/4
std_50_59_nonvet = st.stats.sem(vets_age_df.loc['50-59','Nonvet_suicide_2005':'Nonvet_suicide_2008'])/4
std_60_69_nonvet = st.stats.sem(vets_age_df.loc['60-69','Nonvet_suicide_2005':'Nonvet_suicide_2008'])/4
std_70_79_nonvet = st.stats.sem(vets_age_df.loc['70-79','Nonvet_suicide_2005':'Nonvet_suicide_2008'])/4
std_80_nonvet = st.stats.sem(vets_age_df.loc['80+','Nonvet_suicide_2005':'Nonvet_suicide_2008'])/4
```


```python
# Create lists to store standard deviation calculations
vet_suc_age_list = (vets_age_df['vet_suicide_2005']+vets_age_df['vet_suicide_2006']+
                    vets_age_df['vet_suicide_2007']+vets_age_df['vet_suicide_2008'])
vet_suc_pop = vets_age_df['vet_pop_16sates']
nonvet_suc_age_list = (vets_age_df['Nonvet_suicide_2005']+vets_age_df['Nonvet_suicide_2006']+
                       vets_age_df['Nonvet_suicide_2007']+vets_age_df['Nonvet_suicide_2008'])
nonvet_suc_pop = vets_age_df['nonvet_pop_16sates']
```


```python
# Create new dataframe with lists and rename columns
data = [['18-29',vet_suc_age_list[0],nonvet_suc_age_list[0],vet_suc_pop[0],nonvet_suc_pop[0],std_18_29,std_18_29_nonvet],
        ['30-39',vet_suc_age_list[1],nonvet_suc_age_list[1],vet_suc_pop[1],nonvet_suc_pop[1],std_30_39,std_30_39_nonvet],
        ['40-49',vet_suc_age_list[2],nonvet_suc_age_list[2],vet_suc_pop[2],nonvet_suc_pop[2],std_40_49,std_40_49_nonvet],
        ['50-59',vet_suc_age_list[3],nonvet_suc_age_list[3],vet_suc_pop[3],nonvet_suc_pop[3],std_50_59,std_50_59_nonvet],
        ['60-69',vet_suc_age_list[4],nonvet_suc_age_list[4],vet_suc_pop[4],nonvet_suc_pop[4],std_60_69,std_60_69_nonvet],
        ['70-79',vet_suc_age_list[5],nonvet_suc_age_list[5],vet_suc_pop[5],nonvet_suc_pop[5],std_70_79,std_70_79_nonvet],
        ['80+',vet_suc_age_list[6],nonvet_suc_age_list[6],vet_suc_pop[6],nonvet_suc_pop[6],std_80,std_80_nonvet]]
data_df = pd.DataFrame(data,columns=['Age Group','Total Vet Suicide','Total Non-Vet Suicide','Veterans Population',
                                     'Non-Veterans Population','Vet Std Error','Non-Vet Std Error'])
final_data = data_df.set_index('Age Group')
vet_rate = ((final_data['Total Vet Suicide']/final_data['Veterans Population'])*100000)/4
non_vet_rate = ((final_data['Total Non-Vet Suicide']/final_data['Non-Veterans Population'])*100000)/4
vet_rate.round(2)
non_vet_rate.round(2)
final_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Vet Suicide</th>
      <th>Total Non-Vet Suicide</th>
      <th>Veterans Population</th>
      <th>Non-Veterans Population</th>
      <th>Vet Std Error</th>
      <th>Non-Vet Std Error</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18-29</th>
      <td>61</td>
      <td>2307</td>
      <td>65974</td>
      <td>4442150</td>
      <td>0.679882</td>
      <td>44.821332</td>
    </tr>
    <tr>
      <th>30-39</th>
      <td>329</td>
      <td>3490</td>
      <td>302379</td>
      <td>4997418</td>
      <td>1.077105</td>
      <td>1.386317</td>
    </tr>
    <tr>
      <th>40-49</th>
      <td>748</td>
      <td>4068</td>
      <td>544281</td>
      <td>4804281</td>
      <td>0.677003</td>
      <td>2.917262</td>
    </tr>
    <tr>
      <th>50-59</th>
      <td>1921</td>
      <td>4249</td>
      <td>808175</td>
      <td>4852566</td>
      <td>2.325974</td>
      <td>4.472573</td>
    </tr>
    <tr>
      <th>60-69</th>
      <td>1913</td>
      <td>2241</td>
      <td>1412933</td>
      <td>2969481</td>
      <td>9.483195</td>
      <td>25.705742</td>
    </tr>
    <tr>
      <th>70-79</th>
      <td>2006</td>
      <td>1065</td>
      <td>1094061</td>
      <td>1424385</td>
      <td>5.553246</td>
      <td>13.486249</td>
    </tr>
    <tr>
      <th>80+</th>
      <td>2936</td>
      <td>595</td>
      <td>1269990</td>
      <td>627695</td>
      <td>13.080281</td>
      <td>5.115718</td>
    </tr>
  </tbody>
</table>
</div>




```python
grand_total_vet_suicide = final_data["Total Vet Suicide"].sum()
percent_vet_suicide = (final_data["Total Vet Suicide"]/grand_total_vet_suicide)*100
suicide_percentage = percent_vet_suicide.round(2)

# Plot Bar Chart for final_data
N = 7
ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind,vet_rate, width, color='green', yerr=0.2*final_data['Vet Std Error'])


rects2 = ax.bar(ind+width, non_vet_rate, width, color='skyblue', yerr=0.2*final_data['Non-Vet Std Error'])

# Add some text for labels, title and axes ticks
ax.set_ylabel('Suicide Rate per 100,000 Population')
ax.set_xlabel('Age Group')
ax.set_title('Suicide Rate by Age Group')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('18-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+'))
plt.ylim(0,90,10)
ax.legend((rects1[0], rects2[0]), ('Veteran', 'Non-Veteran'))
sns.set(rc={'figure.figsize':(12,7)})

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.25*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
plt.savefig("Suicide_by_Age_Group")
plt.show()
```


![png](output_32_0.png)



```python
# Plot pie chart
plt.figure(figsize=(5,5))
plt.title("Percentage of Veterans Suicide by Age Group")
colors = ['green', 'yellowgreen', 'lightskyblue', 'darksalmon','royalblue','darkgray']
explode = (0, 0, 0, 0, 0, 0.1)
plt.pie(
    [percent_vet_suicide['30-39'],percent_vet_suicide['40-49'],percent_vet_suicide['50-59'],percent_vet_suicide['60-69'],percent_vet_suicide['70-79'],percent_vet_suicide['80+']],
    explode=explode,colors = colors,
    labels=["30-39","40-49","50-59","60-69","70-79","80+"],
    autopct='%.2f',
    pctdistance=.6,shadow=True)
plt.axis('equal')
plt.savefig("Percent_Vet_Suicide_Age_Group")
plt.show()
```


![png](output_33_0.png)



```python
sns.set(style="whitegrid")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(4, 3))

# Load the dataset
y_pos = ["40-59","60-69","70-79","80+"]
x_pos =[suicide_percentage['50-59'],suicide_percentage['60-69'],suicide_percentage['70-79'],suicide_percentage['80+']]
# Plot the Suicide rate
sns.set_color_codes("pastel")
sns.barplot(x_pos, y_pos,
            label="Percentage", palette="Blues")
plt.xlim(0,30,10)

for i, v in enumerate(x_pos):
    plt.text(v + 3, i + .25, str(v), color='black', fontweight='bold', fontsize = 12 )

# Add a legend and informative axis label

plt.xlabel("Veteran Suicide Percentage")
plt.ylabel("Age Group")
sns.despine(left=True, bottom=True)
plt.savefig("Veteran_Sucide_Rate")
plt.show()


size_of_groups=[70,30]
f, ax = plt.subplots(figsize=(3, 3))
# Create a pieplot
plt.pie(size_of_groups)
#plt.show()
text = '69.14%'
# add a circle at the center
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
kwargs = dict(size=20, fontweight='bold', va='center')
ax.text(0, 0, text, ha='center', **kwargs)
plt.title("Veterans over age 55 account for 69.14% of all veterans suicides",fontsize = 14)
interactive(False)
plt.savefig("Vet_Suicides_Over55_Age_Group")
plt.show()
```


![png](output_34_0.png)



![png](output_34_1.png)


## Veteran Suicides by Gender
When analyzing the veteran suicide data by gender, there was noticably a higher rate of suicide among male veterans than female veterans.  The overall average of the rate of male sucides is about forty-three percent.  In the course of ten years (2005-2014), there was an increase of in suicide rates of male veterans by almost ten percent.  Whereas, female veterans suicide rates have been fairly consistent throughout the ten years with an overall average of twelve percent.


```python
# Read and create dataframe for female vets
female_vets_df = pd.read_csv("veteran_data/Vet Suicides 2005-2014 (Females).csv")
female_vets_df = female_vets_df.set_index("female")
female_vets_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2005</th>
      <th>2006</th>
      <th>2007</th>
      <th>2008</th>
      <th>2009</th>
      <th>2010</th>
      <th>2011</th>
      <th>2012</th>
      <th>2013</th>
      <th>2014</th>
    </tr>
    <tr>
      <th>female</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18-29</th>
      <td>6.7</td>
      <td>4.7</td>
      <td>10.2</td>
      <td>5.4</td>
      <td>15.2</td>
      <td>11.1</td>
      <td>19.3</td>
      <td>12.9</td>
      <td>15.7</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>30-39</th>
      <td>13.8</td>
      <td>10.9</td>
      <td>15.7</td>
      <td>15.9</td>
      <td>14.9</td>
      <td>15.3</td>
      <td>13.5</td>
      <td>14.4</td>
      <td>17.4</td>
      <td>17.6</td>
    </tr>
    <tr>
      <th>40-49</th>
      <td>27.4</td>
      <td>7.8</td>
      <td>14.8</td>
      <td>12.8</td>
      <td>16.7</td>
      <td>17.4</td>
      <td>18.1</td>
      <td>20.3</td>
      <td>20.6</td>
      <td>22.7</td>
    </tr>
    <tr>
      <th>50-59</th>
      <td>7.5</td>
      <td>12.9</td>
      <td>13.8</td>
      <td>25.3</td>
      <td>18.1</td>
      <td>18.8</td>
      <td>18.1</td>
      <td>18.1</td>
      <td>11.8</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>60-69</th>
      <td>4.8</td>
      <td>6.8</td>
      <td>8.6</td>
      <td>4.0</td>
      <td>9.0</td>
      <td>19.4</td>
      <td>14.7</td>
      <td>11.9</td>
      <td>9.7</td>
      <td>14.5</td>
    </tr>
    <tr>
      <th>70-79</th>
      <td>25.9</td>
      <td>5.3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>10.8</td>
      <td>0.0</td>
      <td>10.6</td>
      <td>31.4</td>
      <td>0.0</td>
      <td>14.7</td>
    </tr>
    <tr>
      <th>80+</th>
      <td>15.3</td>
      <td>7.8</td>
      <td>8.2</td>
      <td>17.7</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.2</td>
      <td>0.0</td>
      <td>5.7</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Read and create dataframe for male vets
male_vets_df = pd.read_csv("veteran_data/Vet Suicides 2005-2014 (Males).csv")
male_vets_df = male_vets_df.set_index("male")
male_vets_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2005</th>
      <th>2006</th>
      <th>2007</th>
      <th>2008</th>
      <th>2009</th>
      <th>2010</th>
      <th>2011</th>
      <th>2012</th>
      <th>2013</th>
      <th>2014</th>
    </tr>
    <tr>
      <th>male</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18-29</th>
      <td>27.8</td>
      <td>48.2</td>
      <td>37.4</td>
      <td>48.4</td>
      <td>45.5</td>
      <td>55.4</td>
      <td>60.4</td>
      <td>67.0</td>
      <td>74.6</td>
      <td>73.3</td>
    </tr>
    <tr>
      <th>30-39</th>
      <td>44.7</td>
      <td>44.3</td>
      <td>43.1</td>
      <td>40.0</td>
      <td>45.1</td>
      <td>47.7</td>
      <td>54.3</td>
      <td>49.2</td>
      <td>51.5</td>
      <td>55.5</td>
    </tr>
    <tr>
      <th>40-49</th>
      <td>48.6</td>
      <td>40.8</td>
      <td>49.1</td>
      <td>50.6</td>
      <td>46.4</td>
      <td>44.8</td>
      <td>51.8</td>
      <td>46.6</td>
      <td>46.3</td>
      <td>45.6</td>
    </tr>
    <tr>
      <th>50-59</th>
      <td>39.3</td>
      <td>44.0</td>
      <td>41.5</td>
      <td>45.9</td>
      <td>45.6</td>
      <td>45.8</td>
      <td>50.2</td>
      <td>45.4</td>
      <td>39.4</td>
      <td>43.6</td>
    </tr>
    <tr>
      <th>60-69</th>
      <td>31.1</td>
      <td>32.9</td>
      <td>32.4</td>
      <td>38.1</td>
      <td>32.4</td>
      <td>32.8</td>
      <td>31.1</td>
      <td>30.0</td>
      <td>32.0</td>
      <td>33.1</td>
    </tr>
    <tr>
      <th>70-79</th>
      <td>31.5</td>
      <td>34.7</td>
      <td>30.9</td>
      <td>33.2</td>
      <td>34.0</td>
      <td>32.7</td>
      <td>33.3</td>
      <td>36.4</td>
      <td>42.0</td>
      <td>34.5</td>
    </tr>
    <tr>
      <th>80+</th>
      <td>41.5</td>
      <td>38.0</td>
      <td>38.9</td>
      <td>41.5</td>
      <td>43.0</td>
      <td>36.4</td>
      <td>44.6</td>
      <td>45.7</td>
      <td>44.9</td>
      <td>46.7</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
# Calculate the overall averages in the course of 10 years for male and female vets
male_overall_avg = (sum(male_avgs))/10
female_overall_avg = (sum(female_avgs))/10

# Female vet overall average in course of 10 years
female_overall_avg = (sum(female_avgs))/10
female_overall_avg
# Male vet overall average in course of 10 years
male_overall_avg = (sum(male_avgs))/10
male_overall_avg

# Calculate the total avgs for vets    
total_list = [male + female for male, female in zip(male_avgs, female_avgs)]
total_avg_list = [x / 2 for x in total_list]

# Create a list that holds the years
years_list = ["2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]

# Create new datafame with averages
avgs_df = pd.DataFrame({"Female": female_avgs, "Male": male_avgs, "Year": years_list, "Total Average": total_avg_list})
avgs_df = avgs_df.set_index("Year")
avgs_df.round(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Female</th>
      <th>Male</th>
      <th>Total Average</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2005</th>
      <td>14.49</td>
      <td>37.79</td>
      <td>26.14</td>
    </tr>
    <tr>
      <th>2006</th>
      <td>8.03</td>
      <td>40.41</td>
      <td>24.22</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>10.19</td>
      <td>39.04</td>
      <td>24.61</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>11.59</td>
      <td>42.53</td>
      <td>27.06</td>
    </tr>
    <tr>
      <th>2009</th>
      <td>12.10</td>
      <td>41.71</td>
      <td>26.91</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>11.71</td>
      <td>42.23</td>
      <td>26.97</td>
    </tr>
    <tr>
      <th>2011</th>
      <td>14.21</td>
      <td>46.53</td>
      <td>30.37</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>15.57</td>
      <td>45.76</td>
      <td>30.66</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>11.56</td>
      <td>47.24</td>
      <td>29.40</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>14.36</td>
      <td>47.47</td>
      <td>30.91</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Combine averages into a list for plotting
avgs_list = [male_avgs, female_avgs]
# Give chart title, labels, and ticks
sns.set_style("whitegrid")
plt.title("Average Vet Suicide Rate by Gender (2005-2014)")
plt.xlabel("Year")
plt.ylabel("Average Rate of Suicide per 100,000 Population (%)")
plt.xticks(np.arange(11), years_list)
# Plotting bar chart
x = np.arange(10)
plt.bar(x + 0.00, total_avg_list, color= 'seagreen', width = 0.25, label="Total")
plt.bar(x + 0.25, avgs_list[0], color = 'deepskyblue', width = 0.25, label="Males")
plt.bar(x + 0.50, avgs_list[1], color = 'coral', width = 0.25, label="Females")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.6))
plt.savefig("Vet_Suicide_Gender_Total")
plt.show()
```


![png](output_39_0.png)



```python
# Give chart titles, labels, and limits
plt.title("Average Vet Suicides Rate by Gender (2005-2014)")
plt.xlabel("Year")
plt.ylabel("Average Rate of Suicide per 100,000 Population (%)")
#plt.xlim(2005, 2014)
plt.ylim(5, 50)
# Create handles for legend and plot line graph with grid
Female, = plt.plot(years_list, female_avgs, marker="o", color="coral", label="Females")
Male, = plt.plot(years_list, male_avgs, marker="s", color="deepskyblue", label="Males")
plt.legend(handles=[Female, Male], loc='center left', bbox_to_anchor=(1, 0.6))
plt.savefig("Vet_Suicides_Gender")
plt.show()
```


![png](output_40_0.png)

