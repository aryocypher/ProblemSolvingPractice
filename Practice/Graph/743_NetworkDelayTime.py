# 743. Network Delay Time
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

# Example 1:


# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Example 2:

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:

# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
 

# Constraints:

# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList=[[] for i in range(n+1)]
        for curr in times:
            adjList[curr[0]].append([curr[1],curr[2]])
        pq=[]
        heapq.heappush(pq,(0,k))
        dist=[sys.maxsize for _ in range(n+1)]
        dist[k]=0
        print(dist)
        print(adjList)
        while pq:
            curr=heapq.heappop(pq)
            for nbr in adjList[curr[1]]:
                print(nbr)
                if dist[nbr[0]]>curr[0]+nbr[1]:
                    dist[nbr[0]]=curr[0]+nbr[1]
                    heapq.heappush(pq,(dist[nbr[0]] ,nbr[0]))

        maxVal=max(dist[1:])
        return maxVal if maxVal!=sys.maxsize else -1
