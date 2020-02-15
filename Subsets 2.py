#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Subsets 2(leetcode 90)


# In[ ]:


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        nums.sort()
        for num in nums:
            result += [i + [num] for i in result]
            x= []
            for i in result:
                if i not in x:
                    x.append(i)
    
        return x
        

