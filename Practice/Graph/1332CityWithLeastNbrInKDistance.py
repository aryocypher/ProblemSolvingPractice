# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
# Solved
# Medium
# Topics
# Companies
# Hint
# There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

# Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

 

# Example 1:


# Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
# Output: 3
# Explanation: The figure above describes the graph. 
# The neighboring cities at a distanceThreshold = 4 for each city are:
# City 0 -> [City 1, City 2] 
# City 1 -> [City 0, City 2, City 3] 
# City 2 -> [City 0, City 1, City 3] 
# City 3 -> [City 1, City 2] 
# Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
# Example 2:


# Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
# Output: 0
# Explanation: The figure above describes the graph. 
# The neighboring cities at a distanceThreshold = 2 for each city are:
# City 0 -> [City 1] 
# City 1 -> [City 0, City 4] 
# City 2 -> [City 3, City 4] 
# City 3 -> [City 2, City 4]
# City 4 -> [City 1, City 2, City 3] 
# The city 0 has 1 neighboring city at a distanceThreshold = 2.
 

# Constraints:

# 2 <= n <= 100
# 1 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 3
# 0 <= fromi < toi < n
# 1 <= weighti, distanceThreshold <= 10^4
# All pairs (fromi, toi) are distinct.

class Solution:
    def findShortestPath(self,n,adjList,src):
        pq=[]
        res=[sys.maxsize]*n
        heapq.heappush(pq,(0,src))
        res[src]=0
        while(pq):
            curr=heapq.heappop(pq)
            for nbr in adjList[curr[1]]:
                if nbr[1]+curr[0]<res[nbr[0]]:
                    res[nbr[0]]=nbr[1]+curr[0]
                    heapq.heappush(pq,(res[nbr[0]],nbr[0]))

        return res

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjList=[[] for _ in range(n)]
        for edge in edges:
            adjList[edge[0]].append([edge[1],edge[2]])
            adjList[edge[1]].append([edge[0],edge[2]])

        res=[]
        for i in range(n):
            res.append(self.findShortestPath(n,adjList,i))

        print(res)
        curr=[0]*n
        for i in range(n):
            for j in range(n):
                if i!=j and res[i][j]<=distanceThreshold:
                    curr[i]+=1


        minVal=sys.maxsize
        city=-1
        for i in range(n):
            if curr[i]<=minVal:
                minVal=curr[i]
                city=i
        
        return city
