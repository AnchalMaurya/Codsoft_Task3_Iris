#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df=pd.read_csv('Iris.csv')
df.head()


# In[3]:


x=df['PetalLengthCm'].values
y=df['PetalWidthCm'].values

plt.scatter(x,y)


# In[4]:


x=df['SepalLengthCm'].values
y=df['PetalWidthCm'].values

plt.scatter(x,y)


# In[5]:


df=pd.read_csv('Iris.csv')

sub_df=df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
sub_df.head()


# In[6]:


sub_df=df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
corr=sub_df.corr()
print(corr)


# In[7]:


plt.figure(figsize=(8,6))

plt.imshow(corr)
plt.xticks(range(len(sub_df.corr().columns)),corr.columns)
plt.yticks(range(len(sub_df.corr().columns)),corr.columns)

plt.show()


# In[ ]:




