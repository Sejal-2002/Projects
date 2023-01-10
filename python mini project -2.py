#!/usr/bin/env python
# coding: utf-8

# # importing libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\HP\Desktop\Ass/Latest Covid-19 India Status(n).csv")
print(df)


# # first 10 rows

# In[2]:


df.head(10)


# # last 10 rows

# In[3]:


df.tail(10)


# # checking null values from columns

# In[4]:


df.isnull().sum(axis=0).sort_values()


# # checking null values from rows

# In[5]:


df.isnull().sum(axis=1).sort_values(ascending=True)


# # total cases in every state

# In[7]:


t=df.groupby('States')['TotalCases'].sum().sort_values(ascending=False)
t


# # mostly no of cases observed in these 10 states 

# In[8]:


m=t.head(10)
m


# # no of cases in each state through graph

# In[9]:


t.plot.bar(figsize=(15,5))
plt.show()


# # recovery rate in each state

# In[10]:


r=df.groupby("States")['Discharged'].sum().sort_values(ascending=False)
r


# # graph of recovery rate

# In[11]:


r.plot.bar(figsize=(15,5))
plt.show()


# # death rate

# In[12]:


d=df.groupby("States")['Deaths'].sum().sort_values(ascending=False)
d


# # death ratio through graph

# In[13]:


d.plot.bar(figsize=(15,5))
plt.show()


# In[ ]:




