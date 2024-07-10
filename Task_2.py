#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
data=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Desktop\\pratice_file.csv")
print(type(data))


# In[31]:


data.info


# In[32]:


data.describe()


# In[33]:


data=data.drop_duplicates()
data


# In[34]:


data.isnull()


# In[35]:


data.isnull().sum()


# In[36]:


data.notnull()


# In[37]:


data.isnull().sum().sum()


# In[38]:


data2=data.fillna(value=0)
data2


# In[39]:


data3=data.fillna(method='pad')
data3


# In[40]:


# filling the null value with the next value 
data4=data.fillna(method='bfill')
data4


# In[41]:


import numpy as np
from scipy import stats


# In[42]:


#detect the outliers using IQR
data2.columns


# In[43]:


data2.drop(['NAME'],axis=1,inplace=True)
data2


# In[44]:


Q1=data2.quantile(0.25)
Q3=data2.quantile(0.75)
IQR=Q3-Q1
print(IQR)


# In[45]:


data2=data2[~((data2<(Q1-1.5*IQR))|(data2>(Q3+1.5*IQR))).any(axis=1)]
data2


# In[46]:


data2.describe()


# In[ ]:




