# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for _ in range(numCourses)]
        indeg=[0]*numCourses
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            indeg[pre[0]]+=1
        
        q=deque()
        visited=set()
        for i,num in enumerate(indeg):
            if num==0:
                visited.add(i)
                q.append(i)
        
        print(q,adj,indeg)
        while q:
            temp=q.popleft()
            print(temp)
            for nbr in adj[temp]:
                if indeg[nbr]>0:
                    indeg[nbr]-=1
                if indeg[nbr]==0 and nbr not in visited:
                    q.append(nbr)
                    visited.add(nbr)
        return False if(sum(indeg))>0 else True