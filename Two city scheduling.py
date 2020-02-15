#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Two City Scheduling (Leetcode 1029)


# In[ ]:


class Solution:
    def twoCitySchedCost(self, costs):
        #sortCost = [[costs[i][0]- costs[i][1] , i] for i in costs].split()
        costs.sort(key = lambda cost : cost[0] - cost [1])
        
        sumforA = sum([i[0] for i in costs[:len(costs)//2]])
        sumforB = sum([i[1] for i in costs[len(costs)//2:]])
        return sumforA + sumforB

