#!/usr/bin/env python
# coding: utf-8

# In[178]:


import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#import libraries


#  
# Instructions
# 
# Gary, the VP of Marketing, is looking to spend his marketing budget wisely. He’s asking you to help figure out whom to market to. Gary sent you a list of 1,000 leads that he previously marketed to. (See attached file: leads.csv.)
# 
# Your colleague, Ariana, sent you a list of current clients. (See attached file: Current Clients.xlsx.)
# 
# Gary has his weekly check-in with our CEO Ryan in one hour. He’s asking for a recommendation of where to spend out marketing budget based on the data available.
# 
# Please analyze the attached data sets and send your analysis to Gary along with a recommendation on which type of clients we should market to.
# 
# Please limit the time you spend answering Gary to one hour, or he’ll have to go into the meeting with Ryan without your input. Gary’s tied up in another meeting this hour, and so will not be able to answer any clarifying questions. If there are any ambiguities, please use your best judgement.
# 

# In[179]:


df_lead = pd.read_csv('leads.csv')
df_client = pd.read_csv('current_clients.csv')
#load lead and client files


# In[180]:


df_lead.head()


# In[181]:


df_client.head()


# In[182]:


df_lead.tail()
#need to count all NaN rows


# In[183]:


df_lead.isna().sum().sum()
#64 rows with NaN values
#need to delete all rows


# In[184]:


df_lead.dropna()


# In[185]:


df_client.tail()


# In[186]:


df_client.isna().sum().sum()
#no NaN values in clients csv


# In[187]:


df_lead.dtypes
#need to change debt to a float


# In[188]:


df_lead['debt'] = df_lead['debt'].str.replace('$','')
df_lead['debt'] = df_lead['debt'].str.replace(',', '')
#need to get rid of special characters in the column 'debt'


# In[189]:


df_lead['debt'] = df_lead['debt'].astype(str).astype(float)
#debt column is now a float


# In[190]:


df_lead.head()
#everything looks good now


# In[191]:


df_client.dtypes


# Let's explor the data now

# In[192]:


df_lead.age.hist();
#age range is 20-100


# In[193]:


df_lead.debt.hist();
#debt range is about 10k-110k


# In[194]:


df_client['State'].value_counts()


# In[195]:


df_client.shape[0]


# In[196]:


(19+17+15+13)/180
#36% of the current clients are in Texas, Florida, California, and Ohio 
#New York is 8th on the list for reference


# In[197]:


df_lead['state'].value_counts()


# In[198]:


df_lead.shape[0]


# In[199]:


(112+97+69+50+45)/1000
#37% of the leads are in California, Texas, Florida, New York, and Ohio


# 35% of the current clients reside in Texas, Florida, California, and Ohio respectfully. 37% of the leads reside in California, Texas, Florida, New York, and Ohio respectfully. New York is number 8 on the current client list but number 4 on the leads list.

# In[200]:


#need to seperate age groups in leads
twenties = df_lead[(df_lead['age']>=20) & (df_lead['age']<=29)]
thirties = df_lead[(df_lead['age']>=30) & (df_lead['age']<=39)]
fourties = df_lead[(df_lead['age']>=40) & (df_lead['age']<=49)]
fifties = df_lead[(df_lead['age']>=50) & (df_lead['age']<=59)]
sixties = df_lead[(df_lead['age']>=60) & (df_lead['age']<=69)]
seventies = df_lead[(df_lead['age']>=70) & (df_lead['age']<=79)]
eighties = df_lead[(df_lead['age']>=80) & (df_lead['age']<=89)]
ninties = df_lead[(df_lead['age']>=90) & (df_lead['age']<=99)]
hundred = df_lead[df_lead['age']==100]


# In[201]:


twenties.shape[0]
#the number of people in their 20s


# In[202]:


twenties.debt.hist();


# In[203]:


thirties.shape[0]
#30s


# In[204]:


thirties.debt.hist();


# In[205]:


fourties.shape[0]
#40s


# In[206]:


fourties.debt.hist();


# In[207]:


fifties.shape[0]
#50s


# In[208]:


fifties.debt.hist();


# In[209]:


sixties.shape[0]
#60s


# In[210]:


sixties.debt.hist();


# In[211]:


seventies.shape[0]
#70s


# In[212]:


seventies.debt.hist();


# In[213]:


eighties.shape[0]
#80s


# In[214]:


eighties.debt.hist();


# In[215]:


ninties.shape[0]
#90s


# In[216]:


ninties.debt.hist();


# In[217]:


hundred.shape[0]
#100


# In[218]:


hundred.debt.hist();


# In[219]:


df_lead.nlargest(10, 'debt')
#don't see much of a coorelation with high amount of debt


# In[220]:


plt.figure(figsize = [14,10])
sns.lineplot(data=df_lead, x="age", y="debt")


# There seems to be no coorelation between age and debt amount.

# In[221]:


#let's find out where each decade of people live
twenties['state'].value_counts()
#Texas and California


# In[222]:


thirties['state'].value_counts()
#Texas, Florida, and California


# In[223]:


fourties['state'].value_counts()
#California and Florida


# In[224]:


fifties['state'].value_counts()
#California


# In[225]:


sixties['state'].value_counts()
#Texas, California, and FLorida


# In[226]:


seventies['state'].value_counts()
#California and Texas


# In[227]:


eighties['state'].value_counts()
#California and Ohio


# In[228]:


ninties['state'].value_counts()
#Texas and California


# Notes: Market to California, Texas, Florida, New York, and Ohio.

#  Notes: 20s = TX and CA
# 30s = TX, FL, and CA
# 40s = CA and FL
# 50s = CA
# 60s = TX, CA, and FL
# 70s = CA and TX
# 80s = CA and OH
# 90s = TX and CA

# After exploring the current clients, 35% reside in Texas, Florida, California, and Ohio. 
# In the potential leads 37% reside in California, Texas, Florida, New York, and Ohio.
# The age groups (split by decade for example 20s, 30s, etc.) and amount of debt do not have enough coorlation to investigate further. 
# The top states for all age groups are Texas, Florida, and California. 
# The number of people in each age group are similiar in number as well.
