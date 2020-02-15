#!/usr/bin/env python
# coding: utf-8

# In[2]:


#3. Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1781/Python-solution-with-comments.


# In[5]:


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        count=0
        max_len = 0
        for i , value in enumerate(s):
            if value in dic:
                max_len = max(max_len, i-count)
                
                count = max(count, dic[value] + 1)
            
            dic[value] = i
        
        return max(max_len, len(s) - count)
        


# In[ ]:




