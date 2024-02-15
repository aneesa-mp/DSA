#!/usr/bin/env python
# coding: utf-8

# 1. Find out how many males and females participated in the test.
# 

# In[1]:


import numpy as np
import pandas as pd


# In[5]:


students_data=pd.read_csv(r"C:\Users\anees\Downloads\StudentsPerformance.csv")


# In[6]:


students_data


# In[11]:


gender_count=students_data.groupby('gender').size()


# In[12]:


gender_count['male']


# In[13]:


gender_count['female']


# 2. What do you think about the students' parental level of education

# In[14]:


import matplotlib.pyplot as plt


# In[18]:


parental_education_count=students_data['parental level of education'].value_counts()


# In[19]:


parental_education_count


# In[21]:


plt.bar(students_data['parental level of education'],students_data['math score'],color='red')
plt.title('Distribution of Parental Level of Education')
plt.xlabel('Parental Level of Education')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)


# 3. Who scores the most on average for math, reading and writing based on
# ● Gender
# ● Test preparation course
# 

# In[22]:


average_scores = students_data.groupby(['gender', 'test preparation course']).mean()[['math score', 'reading score', 'writing score']]


# In[23]:


average_scores


# In[ ]:


4. What do you think about the scoring variation for math, reading and writing
based on
● Gender
● Test preparation course


# In[25]:


gender_variation =students_data .groupby('gender').agg({
    'math score': ['mean', 'median', 'std'],
    'reading score': ['mean', 'median', 'std'],
    'writing score': ['mean', 'median', 'std']
})


# In[26]:


gender_variation


# The management needs your help to give bonus points to the top 25% of
# students based on their math score, so how will you help the management
# to achieve this.

# In[29]:


top_25_percentile_math = np.percentile(students_data['math score'], 75)
students_data['bonus_points'] = np.where(students_data['math score'] >= top_25_percentile_math, 5, 0)
print("\nUpdated Dataset with Bonus Points:")
students_data.head()


# In[ ]:




