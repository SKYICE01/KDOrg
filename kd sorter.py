#!/usr/bin/env python
# coding: utf-8

# In[157]:


import warnings 
warnings.filterwarnings('ignore') # optional to handle warnings

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[158]:


df = pd.read_excel('book1.xlsx')

df.head(5)


# In[159]:


df.drop(labels="Alliance",axis=1,inplace=True)


# In[160]:


df.drop(labels="#",axis=1,inplace=True)


# In[161]:


df.drop(labels="Governor ID",axis=1,inplace=True)


# In[162]:


df.head(5)


# In[163]:


n = 367
 

df.drop(df.tail(n).index,
        inplace = True)


# In[164]:


df["Power"].describe().apply(lambda x: format(x, 'f'))


# In[165]:


df["Dead Troops"].describe().apply(lambda x: format(x, 'f'))


# In[166]:


df["T5-Kills"].describe().apply(lambda x: format(x, 'f'))


# In[167]:


df["T4-Kills"].describe().apply(lambda x: format(x, 'f'))


# In[168]:


q1_power=np.percentile(df["Power"], 40)
q2_power = np.percentile(df["Power"], 79)
q3_power=np.percentile(df["Power"], 100)
q2_power


# In[169]:


q1_dead=np.percentile(df["Dead Troops"], 40)
q2_dead=np.percentile(df["Dead Troops"], 79)
q3_dead=np.percentile(df["Dead Troops"], 100)


# In[170]:


q1_t5=np.percentile(df["T5-Kills"], 40)
q2_t5=np.percentile(df["T5-Kills"], 79)
q3_t5=np.percentile(df["T5-Kills"], 100)


# In[171]:


q1_t4=np.percentile(df["T4-Kills"], 40)
q2_t4=np.percentile(df["T4-Kills"], 79)
q3_t4=np.percentile(df["T4-Kills"], 100)


# In[172]:


df.info()


# In[173]:


df.loc[(df['Power'] <= q1_power),"Power_rank"]=1
df.loc[(df['Power'] > q1_power) & (df['Power'] <= q2_power), 'Power_rank'] = 2
df.loc[(df['Power'] > q2_power) & (df['Power'] <= q3_power), 'Power_rank'] = 3



# In[174]:


df.loc[(df['Dead Troops'] <= q1_dead),"Dead_rank"]=1
df.loc[(df['Dead Troops'] > q1_dead) & (df['Dead Troops'] <= q2_dead), 'Dead_rank'] = 2
df.loc[(df['Dead Troops'] > q2_dead) & (df['Dead Troops'] <= q3_dead), 'Dead_rank'] = 3


# In[175]:


df.loc[(df['T5-Kills'] <= q1_t5),"T5_rank"]=1
df.loc[(df['T5-Kills'] > q1_t5) & (df['T5-Kills'] <= q2_t5), 'T5_rank'] = 2
df.loc[(df['T5-Kills'] > q2_t5) & (df['T5-Kills'] <= q3_t5), 'T5_rank'] = 3


# In[176]:


df.loc[(df['T4-Kills'] <= q1_t4),"T4_rank"]=1
df.loc[(df['T4-Kills'] > q1_t4) & (df['T4-Kills'] <= q2_t4), 'T4_rank'] = 2
df.loc[(df['T4-Kills'] > q2_t4) & (df['T4-Kills'] <= q3_t4), 'T4_rank'] = 3


# In[177]:


#sum each row of columns dead_rank, power_rank, t5_rank, t4_rank
df["rank"]=df[["Dead_rank","Power_rank","T5_rank","T4_rank"]].sum(axis=1)


# In[178]:


#sort based on rank descending
df.sort_values(by=["rank"],ascending=False,inplace=True)

        




# In[179]:


#make a for loop for the size of df.coount and increment it bt 4
for i in range(0,df['rank'].count(),4):
    df.loc[i,"Alliance"]=1
    df.loc[i+1,"Alliance"]=2
    df.loc[i+2,"Alliance"]=3
    df.loc[i+3,"Alliance"]=4

df.head(20)


# In[180]:


#export to excel called rankersorter.xlsx
df.to_excel("rankersorter.xlsx")

