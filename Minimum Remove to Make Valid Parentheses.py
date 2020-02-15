#!/usr/bin/env python
# coding: utf-8

# In[7]:


#1249. Minimum Remove to Make Valid Parentheses


# In[8]:


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, opened, closed = [], 0 , 0
        for i in s:
            if i == '(':
                opened += 1
                stack.append(i)
            elif i== ')':
                if closed < opened:
                    closed+=1
                    stack.append(i)
            else:
                stack.append(i)
                
        res, closed, opened = '', 0,0
        while stack:
            s = stack.pop()
            if s == ')':
                closed+=1
                res = s + res
            elif s == '(':
                if opened < closed:
                    opened+=1
                    res = s + res
            else:
                res = s+ res
        return res
                        
            


# In[ ]:




