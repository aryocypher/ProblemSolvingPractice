class Solution:

    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited = set()
        res = []

        def dfs(val):
            if val in visited:
                return
            res.append(val)
            visited.add(val)

            for nbr in adj[val]:
                dfs(nbr)

            return

        dfs(0)
        return res
