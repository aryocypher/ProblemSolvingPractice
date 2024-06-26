# 787. Cheapest Flights Within K Stops
# Solved
# Medium
# Topics
# Companies
# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

# Example 1:


# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
# Example 2:


# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
# Example 3:


# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 

# Constraints:

# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 104
# There will not be any multiple flights between two cities.
# 0 <= src, dst, k < n
# src != dst
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList=[[] for i in range(n)]
        for flight in flights:
            adjList[flight[0]].append([flight[1],flight[2]])
        
        dist=[sys.maxsize for _ in range(n)]
        q=deque()
        q.append((0,src,-1))
        dist[src]=0

        while q:
            curr=q.popleft()
            for nbr in adjList[curr[1]]:
                if dist[nbr[0]]>curr[0]+nbr[1] and curr[2]+1<=k:
                    dist[nbr[0]]=curr[0]+nbr[1]
                    q.append((dist[nbr[0]],nbr[0],curr[2]+1))
            print(curr,dist)

        return -1 if dist[dst]==sys.maxsize else dist[dst]

        



        

