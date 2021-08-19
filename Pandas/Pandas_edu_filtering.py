#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd


# In[73]:


df = pd.read_csv('survey_results_public.csv')
schema_df = pd.read_csv('survey_results_schema.csv')


# In[74]:


schema_df


# In[78]:


filt = (schema_df['Column'] == 'Hobbyist') & (schema_df['QuestionText'] == 'Do you code as a hobby?') # mixed and conditional


# In[79]:


schema_df.loc[filt, 'QuestionText']


# In[80]:


filt = (schema_df['Column'] == 'Hobbyist') | (schema_df['QuestionText'] == 'In which country do you currently reside?') # mixed or conditional


# In[81]:


schema_df.loc[filt, 'QuestionText']


# In[82]:


schema_df.loc[~filt, 'QuestionText'] # return opposite values 


# In[83]:


high_salary = (df['ConvertedComp'] > 70000)


# In[86]:


df.loc[high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']]


# In[88]:


df.loc[df.ConvertedComp > 70000][df.Country == 'United States']


# In[89]:


countries = ['United States', 'India', 'United Kingdom']
filt = df['Country'].isin(countries)


# In[90]:


df.loc[filt, 'Country']


# In[97]:


df['LanguageWorkedWith'].str.contains('Python', na=False) # filt every rows with python in selected column


# In[102]:


df.loc[filt]['LanguageWorkedWith']


# In[ ]:




