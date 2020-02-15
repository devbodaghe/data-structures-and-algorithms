#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Subsets 1(leetcode 78)


# In[ ]:


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result

