#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Minimum absolute difference (Leetcode 1200)


# In[3]:


class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        result = []
        min_diff  = sys.maxsize
        for i, value in enumerate(arr[0:len(arr) - 1]):
            if arr[i+1] - value < min_diff:
                min_diff = arr[i+1] - value
                result = [[value, arr[i+1]]]
            elif arr[i+1] - value == min_diff:
                result.append([value, arr[i+1]])
        return result
    


# In[ ]:




