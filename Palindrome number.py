#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Palindrome - https://leetcode.com/problems/palindrome-number/


# In[6]:


class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        if x < 0:
            return False
        if x == 0:
            return True
        rev = 0
        while(x > 0):
            a = x % 10
            rev = rev * 10 + a 
            x = x // 10
        return y == rev
    


# In[ ]:




