#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[11]:


neg = pd.read_csv('comments_negative.csv')  


# In[12]:


pos = pd.read_csv('comments_positive.csv')


# In[178]:


frames = [pos, neg]

final = pd.concat(frames)


# In[179]:


final# = final.sample(n=5000000)


# In[182]:


#def scale_list(l, to_min, to_max):
#    arr = np.array(l)
#    scaled_arr = (arr - arr.min()) * (to_max - to_min) / (arr.max() - arr.min()) + to_min
#    return list(np.round(scaled_arr).astype(int))

final['score_scaled'] = pd.qcut(final.score,[0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1], labels=['1','2','3','4','5','6','7','8','9','10'])


# In[184]:


final.groupby(['score_scaled'])['text'].count()


# In[185]:


#final["score_scaled"] = scale_list(final["score"], 1, 10)

#final["score_scaled"] = [scale_list(final["score"], 1, 10) for score in final["score"]]


# In[186]:


#PICK UP FROM HERE IF MISTAKE

final_dropped = final.drop(columns=['id', 'parent_id', 'parent_link_id', 'subreddit_id', 'link_id', 'score', 'ups', 'author', 'controversiality', 'parent_ups', 'parent_author', 'parent_text', 'parent_score', 'parent_controversiality'])


# In[187]:


sampled = final_dropped.sample(n=60000, random_state = 5422)


# In[188]:


sampled['text'] = sampled['text'].str.replace('\W', ' ', regex=True)


# In[190]:


sampled.groupby(['score_scaled'])['text'].count()


# In[192]:


sampled.to_csv("reddit_comments.csv", index=False)


# In[ ]:




