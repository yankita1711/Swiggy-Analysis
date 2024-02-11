#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import warnings
warnings.filterwarnings(action='ignore')


# In[2]:


df_swiggy = pd.read_csv("Swiggy Bangalore Outlet Details.csv")


# In[3]:


df_swiggy


# In[4]:


df_swiggy.info()


# In[5]:


df_swiggy.isnull().sum()


# In[6]:


df_swiggy.describe()


# In[7]:


pip install -U dataprep


# In[8]:


df_swiggy.duplicated().sum()


# In[9]:


df_swiggy['Cost_for_Two'].unique()


# In[10]:


df_swiggy['Cost_for_Two']= df_swiggy['Cost_for_Two'].str.replace('₹','').astype(int)
df_swiggy


# In[11]:


df_swiggy.rename(columns={'Cost_for_Two': 'Cost_for_Two(₹)'},inplace=True)
df_swiggy


# In[12]:


df_swiggy['Rating'].unique()


# In[13]:


df_swiggy['Rating']= df_swiggy['Rating'].replace('--','0').astype(float)


# In[14]:


df_swiggy['Rating'].unique()


# In[15]:


df_swiggy.dtypes


# In[16]:


df_swiggy.describe()


# In[17]:


#Observation
#1.Average Cost_for_Two members is Rs321.
#2.Average rating for the restaurants is 4.06.
#3.Max rating and Cost_for_two is 4.8 and Rs800.


# In[23]:


df_swiggy['Location'], df_swiggy['Area'] = df_swiggy['Location'].str.rsplit(', ', 1).str


# In[24]:


df_swiggy.head()


# In[25]:


df_swiggy['Area'].unique()


# In[26]:


df_Koramangala =df_swiggy[df_swiggy['Area'].str.contains('Koramangala')]
df_Koramangala


# In[27]:


df_HSR =df_swiggy[df_swiggy['Area'].str.contains('HSR')]
df_HSR


# In[28]:


df_BTM =df_swiggy[df_swiggy['Area'].str.contains('BTM')]
df_BTM


# In[29]:


sns.displot(df_swiggy[df_swiggy['Rating']>0]['Rating'], kde= True,height = 4)


# In[30]:


# Conclusion
#From this Distribution Plot, We can conclude that More that '50%' of Restaurants are having a Rating greater than "4.1" with a Maximum Rating of "4.8"


# In[32]:


#Area Wise Analysis
#Cost for Two People
# For BTM : cost for two 
plt.figure(figsize=(5,4))
sns.histplot(df_BTM['Cost_for_Two(₹)'], bins = 10)
plt.show()


# In[34]:


# For HSR : cost for two 
plt.figure(figsize=(5,4))
sns.histplot(df_HSR['Cost_for_Two(₹)'], bins = 10)
plt.show()


# In[35]:


#For Koramangala : cost for two 
plt.figure(figsize=(5,4))
sns.histplot(df_Koramangala['Cost_for_Two(₹)'], bins = 15)
plt.show()


# In[36]:


#Area Wise Rating


# In[39]:


# plotting first histogram
plt.hist(df_Koramangala['Rating'], label="Koramangala", alpha=.7,
         edgecolor='black', color='yellow',range=(3.5,4.8))

#second histogram
plt.hist(df_BTM['Rating'], label="BTM", alpha=.7,
         edgecolor='black', color='green',range=(3.5,4.8))

# plotting third histogram
plt.hist(df_HSR['Rating'], label='HSR', alpha=.7, color='red',bins=20,range=(3.5,4.8))
plt.xlabel('Rating ',fontsize=15)
plt.ylabel('Count  ',fontsize=15)
plt.legend()
 
# Showing the plot using plt.show()
plt.show()


# In[40]:


#Conclusion
#1.BTM : Most has 3.9 to 4.1 Rating and Approx. Cost for Two People lies between 200 to 350. (Max. Cost goes upto 600)
#2.HSR : Most has 4 or above Rating and Approx. Cost for Two People lies between 300 to 400. (Max. Cost goes upto 800)
#3.Koramangala : Most has 4.0 to 4.4 Rating and Approx. Cost for Two People lies between 200 to 350. (Max. Cost goes upto 600)


# In[41]:


#Question:High rated restaurants and their cost


# In[42]:


df_Highest_Rated_Restaurants = df_swiggy[df_swiggy['Rating'] >= 4.0]
df_Highest_Rated_Restaurants


# In[43]:


df_Highest_Rated_Restaurants = df_Highest_Rated_Restaurants.loc[:, ['Shop_Name', 'Rating', 'Cost_for_Two(₹)']]
df_Highest_Rated_Restaurants


# In[44]:


df_Highest_Rated_Restaurants = df_Highest_Rated_Restaurants.groupby(['Shop_Name', 'Rating'])['Cost_for_Two(₹)'].agg('mean')
df_Highest_Rated_Restaurants = df_Highest_Rated_Restaurants.reset_index()
df_Highest_Rated_Restaurants


# In[45]:


fig = px.scatter(x=df_Highest_Rated_Restaurants['Cost_for_Two(₹)'], 
                 y=df_Highest_Rated_Restaurants['Rating'], 
                 color=df_Highest_Rated_Restaurants['Rating'],
                size=df_Highest_Rated_Restaurants['Cost_for_Two(₹)'],
                labels = {'x' : 'Approx. Cost_for_Two(₹)', 'y' : 'Rating', 'color' : 'Rating_Indicator'})
fig.update_layout(title = "Analyse 'Approx Cost of 2 People' vs 'Rating'")
fig.show()


# In[46]:


#Revenue Analysis
Revenue={}

Revenue['BTM']=df_BTM['Cost_for_Two(₹)'].sum()
Revenue['HSR']=df_HSR['Cost_for_Two(₹)'].sum()
Revenue['Koramangala']=df_Koramangala['Cost_for_Two(₹)'].sum()

Re=Revenue.values()
city=Revenue.keys()
    
Revenue=pd.DataFrame()
Revenue['Revenue'] = Re
Revenue['City'] = city
Revenue


# In[47]:


sns.barplot(x=Revenue['City'], y=Revenue['Revenue'],data=Revenue)
plt.xlabel('Revenue ',fontsize=15)
plt.ylabel('City    ',fontsize=15)
plt.figure(figsize=(4,4))
plt.show()


# In[48]:


#Conclusion
#High revenue generating area is Koramangala and the Least is HSR.


# In[49]:


#Top 15 Expensive & Highest Rated Restaurants with Approx. Cost for 2 People:


# In[50]:


df_Expensive_Restaurants = df_Highest_Rated_Restaurants.sort_values(by = 'Cost_for_Two(₹)', ascending = False)
df_Expensive_Restaurants


# In[51]:


fig = px.bar(data_frame = df_Expensive_Restaurants, 
             x = df_Expensive_Restaurants['Shop_Name'][0:15], 
             y = df_Expensive_Restaurants['Cost_for_Two(₹)'][0:15], 
             color = df_Expensive_Restaurants['Rating'][0:15], 
            labels = {'x' : 'Restaurant_Name', 'y' : 'Approx. Cost_for_Two (₹)', 'color' : 'Rating'})
fig.update_layout(template = 'plotly_dark', 
                  title = 'Top 15 Expensive & Highest Rated Restaurants with Approx. Cost for 2 People')
fig.show()


# In[52]:


#Analyze Affordable/Budgeted and Highest Rated Restaurants of Bangalore


# In[53]:


df_Affordable_Restaurants = df_swiggy[(df_swiggy['Cost_for_Two(₹)'] <= 500) & (df_swiggy['Rating'] >= 4.0)]
df_Affordable_Restaurants


# In[54]:


df_Affordable_Restaurants.sort_values(by = ['Rating'], ascending = False, inplace = True)
df_Affordable_Restaurants=df_Affordable_Restaurants.head(10)
df_Affordable_Restaurants


# In[55]:


plt.figure(figsize = (18, 7))
sns.barplot(x = df_Affordable_Restaurants['Shop_Name'], y = df_Affordable_Restaurants['Cost_for_Two(₹)'])
plt.title('Top 10 Affordable/Budgeted and Highest Rated Restaurants (Bangalore)', fontsize = 14, fontweight = 'bold', 
          fontstyle = 'italic')
plt.xlabel('Shop_Name', fontsize = 10, fontweight = 'bold')
plt.xlabel('Approx. Cost_for_Two (₹)', fontsize = 10, fontweight = 'bold')
plt.xticks(rotation = 90)
plt.show()


# In[56]:


#Cuisine Analysis


# In[57]:


freq_dict={}
for i in df_swiggy['Cuisine'].unique():
    Cuisines_Lists = i.split(',')
    for Cuisine in Cuisines_Lists:
        Cuisine = Cuisine.lstrip(' ')
        if Cuisine in freq_dict:
            freq_dict[Cuisine] = freq_dict[Cuisine] + 1
        else: 
            freq_dict[Cuisine] = 1
        
print(freq_dict)
print()
print('Total Records: \t', len(freq_dict))


# In[58]:


cuisine = freq_dict.keys()
freq = freq_dict.values()


# In[59]:


df_cusine_analysis = pd.DataFrame()
df_cusine_analysis['Cuisine'] = cuisine
df_cusine_analysis['Count'] = freq


# In[60]:


fig = px.bar(data_frame =df_cusine_analysis, 
            x = df_cusine_analysis['Cuisine'], 
            y = df_cusine_analysis['Count'],  
             color = df_cusine_analysis['Count'], 
            labels = {'x' : 'Cusine', 'y' : 'Count', 'color' : 'Count'})
fig.update_layout(template = 'plotly_dark', 
                  title ="Cuisines Overall Analysis (Bangalore)")
fig.show()


# In[61]:


fig = px.pie(data_frame = df_cusine_analysis, 
             names = df_cusine_analysis['Cuisine'], 
             values = df_cusine_analysis['Count'], 
             title = 'Overall Distribution of Cuisines in Bangalore Restaurants')
fig.update_traces(textposition = 'inside', textinfo = 'percent+label')
fig.show()


# In[62]:


#Conclusion:
#From the above Visualizations, We can say, Most of the Resturants sell "Chinese" which is around '12.9%' followed by "North Indian" & "South Indian" Cuisines which are around '11.8%' & '8.46%'.


# In[63]:


#Cuisine Areawise Analysis


# In[64]:


freq_BTM = {}
for i in df_BTM['Cuisine'].unique():
    Cuisine_List = i.split(',')
    for Cuisine in Cuisine_List:
        Cuisine = Cuisine.lstrip()
        if Cuisine in freq_BTM:
            freq_BTM[Cuisine] = freq_BTM[Cuisine] + 1
        else:
            freq_BTM[Cuisine] = 1
            
print(freq_BTM)
print()
print(len(freq_BTM))


# In[65]:


Cuisine = freq_BTM.keys()
freq = freq_BTM.values()
df_cusine_btm = pd.DataFrame()
df_cusine_btm['Cuisine']=Cuisine
df_cusine_btm['Count']=freq


# In[66]:


fig = px.bar(data_frame =df_cusine_btm, 
            x = df_cusine_btm['Cuisine'], 
            y = df_cusine_btm['Count'],  
             color =  df_cusine_btm['Count'], 
            labels = {'x' : 'Cusine', 'y' : 'Count', 'color' : 'Count'})
fig.update_layout(template = 'plotly_dark', 
                  title ="Cuisines Analysis - BTM (Bangalore)")
fig.show()


# In[67]:


fig = px.pie(data_frame = df_cusine_btm, 
             names = df_cusine_btm['Cuisine'], 
             values = df_cusine_btm['Count'], 
             title = 'Distribution of Cuisines in BTM Bangalore Restaurants')

fig.update_traces(textposition = 'inside', textinfo = 'percent+label')
fig.show()


# In[68]:


#Conclusion:
#From the above Visualizations, We can say, In BTM Area, Most of the Resturants sell "Chinese" which is around '17.1%' followed by "North Indian" & "South Indian" Cuisines which are around '15.2%' & '9.52%'.


# In[69]:


freq_HSR = {}
for i in df_HSR['Cuisine'].unique():
    Cuisine_List = i.split(',')
    for Cuisine in Cuisine_List:
        Cuisine = Cuisine.lstrip()
        if Cuisine in freq_HSR:
            freq_HSR[Cuisine] = freq_HSR[Cuisine] + 1
        else:
            freq_HSR[Cuisine] = 1
            
print(freq_HSR)
print()
print(len(freq_HSR))


# In[70]:


Cuisine = freq_HSR.keys()
freq = freq_HSR.values()
dict_HSR = {
    'Cuisine' : Cuisine,
    'Count' : freq
}

df_Cuisine_HSR = pd.DataFrame(dict_HSR)


# In[71]:


plt.figure(figsize = (20, 8))
sns.barplot(x = df_Cuisine_HSR['Cuisine'], 
            y = df_Cuisine_HSR['Count'], 
            data = df_Cuisine_HSR)

plt.xticks(rotation = 90)

plt.title('Cuisines Analysis - HSR (Bangalore)', fontsize = 14, fontweight = 'bold', fontstyle = 'italic')
plt.xlabel('Cuisine', fontsize = 11, fontweight = 'bold')
plt.ylabel('Number of Restaurants', fontsize = 11, fontweight = 'bold')

plt.show()


# In[72]:


fig = px.pie(data_frame = df_Cuisine_HSR, 
             names = df_Cuisine_HSR['Cuisine'], 
             values = df_Cuisine_HSR['Count'], 
             title = 'Distribution of Cuisines in HSR Bangalore Restaurants')

fig.update_traces(textposition = 'inside', textinfo = 'percent+label')
fig.show()


# In[73]:


#Conclusion:
#From the above Visualizations, We can say, In HSR Area, "North Indian" Cuisines are dominated by around '14.3%' followed by "Chinese" & "South Indian" Cuisines '9.52%' & '9.52%' Restaurants respectively.
#So, We can also infer that - In HSR Area, We may have more "North Indian" people staying there.


# In[74]:


freq_Koramangala = {}
for i in df_Koramangala['Cuisine'].unique():
    Cuisine_List = i.split(',')
    for Cuisine in Cuisine_List:
        Cuisine = Cuisine.lstrip()
        if Cuisine in freq_Koramangala:
            freq_Koramangala[Cuisine] = freq_Koramangala[Cuisine] + 1
        else:
            freq_Koramangala[Cuisine] = 1
            
print(freq_Koramangala)
print()
print(len(freq_Koramangala))


# In[75]:


Cuisine = freq_Koramangala.keys()
freq = freq_Koramangala.values()
dict_Koramangala = {
    'Cuisine' : Cuisine,
    'Count' : freq
}

df_Cuisine_Koramangala = pd.DataFrame(dict_Koramangala)


# In[76]:


plt.figure(figsize = (20, 8))
sns.barplot(x = df_Cuisine_Koramangala['Cuisine'], 
            y = df_Cuisine_Koramangala['Count'], 
            data = df_Cuisine_Koramangala)

plt.xticks(rotation = 90)

plt.title('Cuisines Analysis - Koramangala (Bangalore)', fontsize = 14, fontweight = 'bold', fontstyle = 'italic')
plt.xlabel('Cuisine', fontsize = 11, fontweight = 'bold')
plt.ylabel('Number of Restaurants', fontsize = 11, fontweight = 'bold')

plt.show()


# In[77]:


fig = px.pie(data_frame = df_Cuisine_Koramangala, 
             names = df_Cuisine_Koramangala['Cuisine'], 
             values = df_Cuisine_Koramangala['Count'], 
             title = 'Distribution of Cuisines in Koramangala Bangalore Restaurants')

fig.update_traces(textposition = 'inside', textinfo = 'percent+label')
fig.show()


# In[ ]:


#Conclusion:
#From the above Visualizations, We can say, In Koramangala Area, "Chinese" Cuisines are dominated by around '10.3%' followed by "North Indian" & "South Indian" Cuisines '9.66%' & '7.59%' Restaurants respectively.
#So, We can also infer that Most of the people are fond of the "Chinese" Cuisines.

