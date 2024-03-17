# User function Template for python3

from collections import deque


class Solution:

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here

        indeg = [0]*V

        for nbrs in adj:
            for nbr in nbrs:
                indeg[nbr] += 1

        q = deque()
        visited = set()
        for i, val in enumerate(indeg):
            if val == 0:
                visited.add(i)
                q.append(i)

        if len(q) == 0:
            return True

        while q:
            val = q.popleft()
            for nbr in adj[val]:
                indeg[nbr] -= 1
                if indeg[nbr] == 0 and nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)
        return True if sum(indeg) > 0 else False

    def isCyclic(self, V, adj):
        # code here
        visited = set()
        pathVisited = set()

        def dfs(i):
            if i in pathVisited:
                return True

            if i in visited:
                return False

            pathVisited.add(i)
            visited.add(i)

            for nbr in adj[i]:
                if dfs(nbr):
                    return True

            pathVisited.remove(i)
            return False

        for i in range(V):
            if i not in visited:
                if dfs(i):
                    return True

        return False
