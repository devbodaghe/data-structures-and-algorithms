#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Valid Anagram (Leetcode 242)


# In[4]:


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h = {}
        
        for ch in s:
            if ch not in h:
                h[ch] = 0
            h[ch]+=1
            
        for ch in t:
            if ch not in h:
                h[ch] = 0
            h[ch] -= 1
         
        for key in h:
            if h[key]!=0:
                return False
        return True
Solution().isAnagram('david', 'divan')


# In[ ]:




