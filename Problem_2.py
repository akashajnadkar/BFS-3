'''
Time Complexity - O(V+E), We are visiting all nodes along via the edges
Space Complexity - O(V), at max we will have all vertices in queue/recursive stack

Works on Leetcode
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from  collections import deque
from typing import Optional
class Solution:
    def __init__(self):
        self.hashMap = {} #create a hashMap

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        #DFS
        # self.dfs(node)
        # return self.hashMap[node]

        #BFS
        #put input node in queue to find the neighbors
        queue = deque()
        queue.append(node)
        #create the clone graph node while adding to queue 
        self.clone(node)
        while queue:
            #pop a node from queue add neighbors to queue after creating their clone
            #after creating the clone add the clone node to neighbors of the clone node of the current node being processed
            curr = queue.popleft()
            print(self.hashMap.get(curr).val)
            for child in curr.neighbors:
                if child not in self.hashMap:
                    self.clone(child)
                    queue.append(child)
                newNeighbors = self.hashMap.get(curr).neighbors
                newNeighbors.append(self.hashMap.get(child))
        
        return self.hashMap[node]
    
    def dfs(self, node):
        #check if clone has been created for node else create a clone that is added to map
        if node in self.hashMap:
            return
        self.clone(node)
        #visit the newly clone node
        for child in node.neighbors:
            self.dfs(child)
            #add the newly created node as current node's clone's neighbors
            self.hashMap.get(node).neighbors.append(self.hashMap.get(child))
    
    def clone(self,node):
        if node in self.hashMap:
            return
        else:
            newNode = Node(node.val)
            self.hashMap[node] = newNode

        