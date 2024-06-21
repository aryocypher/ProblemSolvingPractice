
# Shortest path in Undirected Graph
# Difficulty: MediumAccuracy: 49.98%Submissions: 61K+Points: 4
# You are given an Undirected Graph having unit weight of the edges, find the shortest path from src to all the vertex and if it is unreachable to reach any vertex, then return -1 for that vertex.

# Example1:

# Input:
# n = 9, m= 10
# edges=[[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
# src=0
# Output:
# 0 1 2 1 2 3 3 4 4
# Explanation:
# Example2:

# Input:
# n = 4, m= 4
# edges=[[0,0],[1,1],[1,3],[3,0]] 
# src=3
# Output:
# 1 1 -1 0
# Explanation:
# Your Task:
# You don't need to print or input anything. Complete the function shortest path() which takes a 2d vector or array of edges representing the edges of an undirected graph with unit weight, an integer n as the number of nodes, an integer m as a number of edges and an integer src as the input parameters and returns an integer array or vector, denoting the vector of distance from src to all nodes.

# Constraint:
# 1<=n,m<=10000
# 0<=edges[i][j]<=n-1

# Expected Time Complexity: O(N + E), where N is the number of nodes and E is the edges
# Expected Space Complexity: O(N)

from collections import deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        adjList=[[] for i in range(n)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        res=[-1]*n
        
        q=deque()
        q.append((src,0))
        visited=set()
        visited.add(src)
        while q:
            curr=q.popleft()
            res[curr[0]]=curr[1]
            for nbr in adjList[curr[0]]:
                if nbr not in visited:
                    visited.add(nbr)
                    q.append((nbr,curr[1]+1))
    
        
        return res
            
        