#!/usr/bin/env python
# coding: utf-8

# ## Olimpiai statisztikák
# ## Készítette: Szász Kristóf (DCFW6L)

# Az adatok forrása: https://www.kaggle.com/the-guardian/olympic-games?select=summer.csv

# In[1]:


import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
pd.set_option('display.max_columns', None)


# In[2]:


data = pd.read_csv('summer.csv')


# In[3]:


data.head()


# In[4]:


data.isna().sum()


# In[5]:


data[data.Country.isna() == True]


# In[6]:


# Maryam Jusuf Jamal - BRN
data.iloc[29603,4] = "MARYAM, Jusuf Jamal"
data.iloc[29603,5] = "BRN"
# Christine Girard - CAN
data.iloc[31072,4] = "GIRARD, Christine"
data.iloc[31072,5] = "CAN"
# Saeid Mohammadpour - IRI
data.iloc[31091,4] = "MOHAMMADPOUR, Saeid"
data.iloc[31091,5] = "IRI"
# Besik Kudukhov
data.iloc[31110,5] = "RUS"


# In[7]:


data[data.Country.isna() == True]


# In[8]:


print(data.Year.min() , "-tól " , data.Year.max() , "-ig")  


# In[9]:


data.Country.unique().shape[0]


# In[10]:


data.City.groupby(data.City).describe().freq.sort_values(ascending = False).head(5)


# In[11]:


data.Country.groupby(data.Country).describe().freq.sort_values(ascending = False).head(5)


# In[12]:


data.Medal.groupby(data.Country).describe().freq.sort_values(ascending = False).head(5)


# In[13]:


countries = data.Country.unique()
countries.sort()


# In[14]:


MedalTable = pd.DataFrame({'Country':countries, 'Gold':0, 'Silver':0,'Bronze':0, 'Total Points':0,}, index = countries)
MedalTable.index = np.arange(1, len(MedalTable) + 1)
MedalTable


# In[15]:


def medalTablePoints(dataframe):
    if dataframe['Medal'] == 'Gold':
        MedalTable.at[MedalTable.loc[MedalTable.Country == dataframe.Country].index[0], 'Gold'] += 1
        MedalTable.at[MedalTable.loc[MedalTable.Country == dataframe.Country].index[0], 'Total Points'] += 3
    elif dataframe['Medal'] == 'Silver':
        MedalTable.at[MedalTable.loc[MedalTable.Country == dataframe.Country].index[0], 'Silver'] += 1
        MedalTable.at[MedalTable.loc[MedalTable.Country == dataframe.Country].index[0], 'Total Points'] += 2
    elif dataframe['Medal'] == 'Bronze':
        MedalTable.at[MedalTable.loc[MedalTable.Country == dataframe.Country].index[0], 'Bronze'] += 1
        MedalTable.at[MedalTable.loc[MedalTable.Country == dataframe.Country].index[0], 'Total Points'] += 1


# In[16]:


data.apply(medalTablePoints, axis = 1)


# In[17]:


MedalTable = MedalTable.sort_values('Total Points', ascending = False)
MedalTable['Rank'] = range(1,148)


# In[18]:


MedalTable.style.hide_index()


# In[19]:


data.Gender.groupby(data.Gender).describe().freq.sort_values(ascending = False)


# In[20]:


men = data.Gender.groupby(data.Gender).describe().freq.sort_values(ascending = False)[0]
women = data.Gender.groupby(data.Gender).describe().freq.sort_values(ascending = False)[1]


# In[ ]:





# In[21]:


df = pd.DataFrame({'Stats': [men, women]},
                  index=['Férfiak', 'Nők'])
plot = df.plot.pie(y='Stats', 
                   figsize=(5, 5), 
                   title = 'Férfiak-Nők aránya az olimpiákon', 
                   colors = ['darkblue', 'pink'])


# In[22]:


data.Athlete.mode()


# In[23]:


data[data.Gender == 'Men'].Athlete.mode()


# In[24]:


data[data.Gender == 'Women'].Athlete.mode()


# In[25]:


data[(data.Gender == "Men") & (data.Country == "HUN")].mode() 


# In[26]:


data[(data.Gender == "Women") & (data.Country == "HUN")].mode() 


# In[27]:


data[data.Athlete == "GEREVICH, Aladar"]


# In[28]:


data[data.Country == "HUN"].mode()


# In[29]:


data[data.Athlete == "KELETI, Agnes"]


# In[30]:


goldMedalPayOuts = {'Singapore': 1000, 'Indonesia': 746, 'Kazakhstan': 250,
                    'Azerbaijan': 248, 'Italy': 166, 'Hungary': 125, 'Russia': 61,
                    'France': 55, 'USA': 37.5, 'South Africa': 37, 'Germany': 22,
                    'Canada': 15, 'Australia': 13.8} 


# In[31]:


silverMedalPayOuts = {'Singapore': 500, 'Indonesia': 378, 'Kazakhstan': 150,
                    'Azerbaijan': 124, 'Italy': 83, 'Hungary': 89, 'Russia': 38,
                    'France': 22, 'USA': 22.5, 'South Africa': 19, 'Germany': 17,
                    'Canada': 11, 'Australia': 10.35} 


# In[32]:


bronzeMedalPayOuts = {'Singapore': 250, 'Indonesia': 188, 'Kazakhstan': 75,
                    'Azerbaijan': 62, 'Italy': 55, 'Hungary': 71, 'Russia': 26,
                    'France': 14, 'USA': 15, 'South Africa': 7, 'Germany': 11,
                    'Canada': 9, 'Australia': 6.9} 


# In[33]:


goldMedalPayOuts


# In[34]:


silverMedalPayOuts


# In[35]:


bronzeMedalPayOuts


# In[36]:


medalPayouts = pd.DataFrame({'GoldMedalPayOuts':goldMedalPayOuts, 'SilverMedalPayOuts': silverMedalPayOuts,
                             'BronzeMedalPayOuts': bronzeMedalPayOuts})


# In[37]:


medalPayouts = medalPayouts.astype(int)


# In[38]:


medalPayouts.plot(kind = "bar", figsize=(7,7),
            title = 'Hány ezer USD-t ér egy olimpiai érem az egyes országokban', 
            color = ['yellow', 'lightgray', 'orange'])
plt.legend(['Aranyérem', 'Ezüstérem', 'Bronzérem'])


# In[39]:


medalPayouts.plot.bar(stacked = True)


# ### Ezek az adatok csak fizetés után lettek volna letölthetőek csv-be, ezért kézzel vettem fel őket
# #### Forrás: https://www.statista.com/statistics/1090581/olympics-number-athletes-by-gender-since-1896/

# In[40]:


menParticipants = {'1896': 241, '1900': 975, '1904': 645,
                    '1908': 1971, '1912': 2359, '1920': 2561, '1924': 2954,
                    '1928': 2606, '1932': 1206, '1936': 3632, '1948': 3714,
                    '1952': 4436, '1956': 2938, '1960': 4727, '1968': 4473, '1972': 6075,
                    '1976': 4824, '1980': 4064, '1984': 5263, '1988': 6197, '1992': 6652,
                    '1996': 6806, '2000': 6582, '2004': 6296, '2008': 6305, '2012': 5892} 


# In[41]:


womenParticipants = {'1896': 0, '1900': 22, '1904': 6,
                    '1908': 37, '1912': 48, '1920': 65, '1924': 135,
                    '1928': 277, '1932': 126, '1936': 331, '1948': 390,
                    '1952': 519, '1956': 376, '1960': 611, '1968': 678, '1972': 1059,
                    '1976': 1260, '1980': 1115, '1984': 1566, '1988': 2194, '1992': 2704,
                    '1996': 3512, '2000': 4069, '2004': 4329, '2008': 4637, '2012': 4676}


# In[42]:


menAndWomenParticipants = pd.DataFrame({'menParticipants':menParticipants, 'womenParticipants': womenParticipants})


# In[43]:


menAndWomenParticipants = menAndWomenParticipants.astype(int)


# In[44]:


menAndWomenParticipants.plot(kind = "bar", figsize=(15,7),
            title = 'A női és férfi olimpikonok arányának alakulása az évek során', 
            color = ['blue', 'red'], stacked = True)
plt.legend(['Férfiak', 'Nők'])


# In[45]:


menParticipants = pd.DataFrame({'Year': menParticipants})


# In[46]:


womenParticipants = pd.DataFrame({'Year': womenParticipants})


# In[47]:


menParticipants


# In[48]:


womenParticipants


# In[49]:


percentage = womenParticipants/(menParticipants + womenParticipants)


# In[50]:


percentage.plot()
plt.figure(figsize = (15,16))


#     -    Egyes sportágakban melyek a legjobb országok
#     -    Egyes országok mely sportágakban a legjobbak

# In[52]:


data.head()


# In[72]:


data.Discipline.groupby(data.Country).describe().sort_values(by = 'count', ascending = False).top.head(15)


# In[71]:


data.Country.groupby(data.Discipline).describe().sort_values(by = 'count', ascending = False).top.head(15)


# In[75]:


disciplineDf = pd.DataFrame({'Discipline': data.Discipline.groupby(data.Country).describe().sort_values(by = 'count', ascending = False).top.head(15)})


# In[76]:


disciplineDf


# In[77]:


countryDf = pd.DataFrame({'Country':data.Country.groupby(data.Discipline).describe().sort_values(by = 'count', ascending = False).top.head(15)})


# In[78]:


countryDf


# In[ ]:




