#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Word Search (leetcode 79) --> Revisit


# In[9]:


class Solution:
    def exist(self, board, word):
    
        def getNeighbours(row, col):
            neigh = []
            if row - 1>= 0: neigh.append((row -1, col))
            if row+1< len(board) : neigh.append((row+1, col))
            if col-1>= 0:neigh.append((row, col-1))
            if col+1<len(board[0]): neigh.append((row, col+1))

            return neigh

        def dfs(row, col, index):
            if index == len(word) and board[row][col]==word[index]:
                return True
            if board[row][col] != word[index]:
                return False
            
            char = board[row][col]
            board[row][col] = '#'

            for ni, nj in getNeighbours(row, col):
                if dfs(row, col, index+1):
                    return True
                
            board[row][col] = char
            return False
    
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        #return False


# In[ ]:




