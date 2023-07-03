#!/usr/bin/env python
# coding: utf-8

# In[22]:


graph = {'A':['B','D'],
         'B':['C','E'],
         'D':['E','G','H'],
         'E':['C','F']}


# A function to perform a Breadth-Limited search
def BLS(src,target,maxBredth):
  
    if src == target : 
        return True 
    if maxBredth <= 0 : 
        return False
    for i in graph[src]:
            if(BLS(i,target,maxBredth-1)):
                return True
    return False

print('result for BLS',BLS('A','F',4))

# A function to perform a Depth-First Search
def dfs(graph, start, visited=[]): 
    visited.append(start)
    for next in graph[start] - set(visited): 
        dfs(graph, next, visited)
    return visited

print(dfs(graph, '4'))

# A function to perform a Breadth-first Search
def bfs(graph, start):
    visited, queue = [], [start] 
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex] - set(visited)) 
    return 

print(bfs(graph, 'A'))


# In[29]:


graph = {1: set([2, 3]),
         2: set([ 1, 4, 5]),
         3: set([1, 6]),
         4: set([2]),
         5: set([2, 6]),
         6: set([3, 5])}
#Binary three


# A function to perform a breadth-Limited search
def BLS(src,target,maxBredth):
  
    if src == target : 
        return True 
    if maxBredth <= 0 : 
        return False
    for i in graph[src]:
            if(BLS(i,target,maxBredth-1)):
                return True
    return False
  
# A function to perform a Iterative Deepening Search
def IDDFS(src, target, maxDepth):
    for i in range(maxDepth):
        if (DLS(src, target, i)):
            return True
    return False

# A function to perform a Depth-First Search
def dfs(graph, start, visited=[]): 
    visited.append(start)
    for next in graph[start] - set(visited): 
        dfs(graph, next, visited)
    return visited

# A function to perform a Breadth-first Search
def bfs(graph, start):
    visited, queue = [], [start] 
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex] - set(visited)) 
    return visited


print("Which search algorith do you want to use? ")
print("Choose one: \n 1- Breadth-first Search \n 2- Depth-First Search  \n 3- Bredth-limited Search \n 4- Iterative Deepening Search")
value = int(input())

if value == 1:
    print(bfs(graph, 1))
elif value == 2 :
    print(dfs(graph, 1))
elif value == 3: 
    print(" Give me target value: ")
    target = int(input())
    print("Give me maxDepth: ")
    maxDepth = int(input())
    print("Give me start point: ")
    src = int(input())
    print(BLS(src,target,maxDepth))
elif value == 4:
    print(" Give me target value: ")
    target = int(input())
    print("Give me maxDepth: ")
    maxDepth = int(input())
    print("Give me start point: ")
    src = int(input())
    print(IDDFS(src, target, maxDepth)) 


# In[ ]:




