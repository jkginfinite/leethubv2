"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        #dictionary to save visited node and its respective clone to avoid cycles
        visited = {}

        #put the first node in the queue
        queue = deque([node])
        #clone the node and put it in the visited dictionary
        visited[node] = Node(node.val,[])

        #start a BFS traversal
        while queue:
            #pop a node say "n" from he left from the front of the queue
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    #clone the neighbor and put in the visited, if not present 
                    visited[neighbor] = Node(neighbor.val,[])
                    #add the newly encountered node to the queue
                    queue.append(neighbor)
                #add the clone of the neighbor to the neighbors of the clone node
                visited[n].neighbors.append(visited[neighbor])

        #return the clone of the node from the visited
        return visited[node]

        #strategy: put the original node into a queue. make an empty dictionary
        #as we go through the queue, save each node to the dictionary using the Node() class by copying the values
        #of the queue into each Node(val) and being saved into the dictionary visited[node] = Node(node.val,[])