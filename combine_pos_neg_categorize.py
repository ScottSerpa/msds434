#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[11]:


neg = pd.read_csv('comments_negative.csv')  


# In[12]:


pos = pd.read_csv('comments_positive.csv')


# In[54]:


frames = [pos, neg]

final = pd.concat(frames)


# In[56]:


final = final.sample(n=100000)


# In[60]:


def scale_number(unscaled, to_min, to_max, from_min, from_max):
    return round((to_max-to_min)*(unscaled-from_min)/(from_max-from_min)+to_min)

def scale_list(l, to_min, to_max):
    return [scale_number(i, to_min, to_max, min(l), max(l)) for i in l]


# In[61]:


final["score_scaled"] = scale_list(final["score"], 1, 10)


# In[70]:


final_dropped = final.drop(columns=['id', 'parent_id', 'parent_link_id', 'subreddit_id', 'link_id', 'score', 'ups', 'author', 'controversiality', 'parent_ups', 'parent_author'])


# In[78]:


sampled = final_dropped.sample(n=60000)


# In[79]:


sampled.to_csv("reddit_comments.csv", index=False)

