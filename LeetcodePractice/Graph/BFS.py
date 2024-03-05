from typing import List
from queue import Queue
from collections import deque


class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        res = []

        q = deque()
        q.append(0)
        visited = set()
        visited.add(0)

        while len(q) > 0:
            temp = q.popleft()
            res.append(temp)

            for val in adj[temp]:
                if val not in visited:
                    q.append(val)
                    visited.add(val)

        return res
