#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1D Candy Crush


# In[ ]:


def removeThree(s):
    i = 0
    while i <= len(s)-4:
        
        # Removes all repeated chars greater than 3
        while s[i] == s[i+1] == s[i+2] == s[i + 3]:
            s = s[:i+3] + s[i+4:]
        
        # Removes repeated chars of 3
        if s[i] == s[i+1] == s[i+2]:
            s = s[:i] + s[i+3:]
            
            # Checks for repeat chars behind the pointer (i)
            if i >= 2 and s[i] == s[i-1] == s[i-2]:
                i -= 2
        
        # Steps forward through string
        else:
            i += 1
    return s

