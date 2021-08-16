#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df = pd.read_csv('survey_results_public.csv')


# In[5]:


df


# In[6]:


df.shape # size of dataframe


# In[12]:


df.shape[0] # number of rows


# In[13]:


df.shape[1] # number of columns


# In[15]:


df.info() # detail info about selected dataframe


# In[16]:


pd.set_option('display.max_columns', 85) # to display 85 columns


# In[17]:


df


# In[19]:


schema_df = pd.read_csv('survey_results_schema.csv')


# In[20]:


schema_df


# In[22]:


pd.set_option('display.max_rows', len(schema_df)) # to display all of dataframe's rows


# In[23]:


schema_df


# In[24]:


df.head(10) # to show first 10 rows


# In[25]:


df.tail(10) # to show last 10 rows


# In[ ]:




