#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd


# In[28]:


df = pd.read_csv('survey_results_public.csv')
schema_df = pd.read_csv('survey_results_schema.csv')


# In[30]:


pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


# In[31]:


df.head()


# In[32]:


schema_df


# In[34]:


df.MainBranch # display selected column


# In[36]:


df[['MainBranch','Hobbyist']] # to display both selected column


# In[37]:


df.columns # to show names of columns in dataframe


# In[38]:


df.iloc[0][2] # to show ceil by number of rows and column


# In[39]:


df.iloc[[0, 1]] # to show 2 rows


# In[43]:


df.iloc[[0,1], 2]


# In[57]:


df.iloc[[0],[1]]


# In[53]:


df.loc[[0,1], ['MainBranch','Hobbyist']]


# In[59]:


df.shape


# In[60]:


df['Hobbyist'].value_counts() # to show statistics uptake from specified column


# In[62]:


df.loc[0, 'Hobbyist']


# In[63]:


df.loc[[0,1,2], 'Hobbyist'] # to show three rows in selected column


# In[65]:


df.loc[0:2, 'Hobbyist':'Employment'] # to show range of rows in set range of columns


# In[66]:


df.set_index('Hobbyist', inplace=True)


# In[67]:


df.reset_index(inplace=True)


# In[68]:


df


# In[69]:


df.set_index('index', inplace=True)


# In[70]:


df


# In[71]:


df.head()


# In[72]:


schema_df.sort_index # to sort indexes alphabetically (not permament withouth inplace=True)


# In[ ]:




