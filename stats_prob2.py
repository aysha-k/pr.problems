#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[17]:


#dataset 1
diamonds=pd.read_csv(r"C:\Users\pc\Desktop\__pycache__\seaborn-data\diamonds.csv")
diamonds


# Range

# In[18]:


depth=diamonds['depth']
Range=depth.max()-depth.min()
Range


# In[19]:


variance=diamonds['depth'].var()
variance


# 
# Standard deviation

# In[20]:


depth_mean=diamonds['depth'].mean()
depth_std=depth.std()
depth_std


# In[21]:


first_std_upperBound = depth_mean + depth_std
print(first_std_upperBound)
first_std_lowerBound = depth_mean - depth_std
print(first_std_lowerBound)


# In[24]:


second_std_upperbound = depth_mean + 2*depth_std
print(second_std_upperbound)
second_std_lowerbound = depth_mean - 2*depth_std
print(second_std_lowerbound)


# In[25]:


third_std_upperbound = depth_mean + 3*depth_std
print(third_std_upperbound)
third_std_lowerbound = depth_mean - 3*depth_std
print(third_std_lowerbound)


# In[26]:


#dataset 2
taxis=pd.read_csv(r"C:\Users\pc\Desktop\__pycache__\seaborn-data\taxis.csv")
taxis


# Range

# In[29]:


tip=taxis['tip']
tip_range =tip.max() -tip.min()
tip_range


# Variance

# In[30]:


tip_variance =taxis['tip'].var()
tip_variance


# Standard deviation

# In[31]:


tip_mean = taxis['tip'].mean()
tip_std = taxis['tip'].std()


# In[32]:


first_std_upperBounce = tip_mean + tip_std
print(first_std_upperBounce)
first_std_lowerBounce = tip_mean - tip_std
print(first_std_lowerBounce)


# In[33]:


second_std_upperBounce = tip_mean + 2*tip_std
print(second_std_upperBounce)
second_std_lowerBounce = tip_mean - 2*tip_std
print(second_std_lowerBounce)


# In[34]:


third_std_upperBounce = tip_mean + 3*tip_std
print(third_std_upperBounce)
third_std_lowerBounce = tip_mean - 3*tip_std
print(third_std_lowerBounce)


# In[35]:


#dataset 3
dots =pd.read_csv(r"C:\Users\pc\Desktop\__pycache__\seaborn-data\dots.csv")
dots


# Range

# In[37]:


coherence = dots['coherence']
coherence_range = coherence.max() - coherence.min()
coherence_range


# Variance

# In[56]:


coh_variance =dots['coherence'].var()
coh_variance


# Standard deviation

# In[42]:


coherence_mean = dots['coherence'].mean()
coherence_std = dots['coherence'].std()


# In[45]:


first_std_upperbounce = coherence_mean + coherence_std
first_std_lowerbounce = coherence_mean - coherence_std
print(f"1st upper bound standered deviation is {first_std_upperbounce}")
print(f"1st lower bound standered deviation is {first_std_lowerbounce}")


# In[46]:


second_std_upperbounce = coherence_mean + 2*coherence_std
second_std_lowerbounce = coherence_mean - 2*coherence_std
print(f"2nd upper bound standered deviation is {second_std_upperbounce}")
print(f"2nd lower bound standered deviation is {second_std_lowerbounce}")


# In[47]:


third_std_upperbounce = coherence_mean + 3*coherence_std
third_std_lowerbounce = coherence_mean - 3*coherence_std
print(f"3rd upper bound standered deviation is {third_std_upperbounce}")
print(f"3rd lower bound standered deviation is {third_std_lowerbounce}")


# In[ ]:




