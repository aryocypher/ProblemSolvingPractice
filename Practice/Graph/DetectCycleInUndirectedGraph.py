def isCycleBFS(self, V: int, adj: List[List[int]]) -> bool:
    # Code here
    visited = [0]*(V)

    def detectCycleBfs(val):
        visited[val] = 1
        q = deque()
        q.append((val, -1))

        while q:
            temp = q.popleft()
            node = temp[0]
            parent = temp[1]

            for nbr in adj[node]:
                if visited[nbr] != 1:
                    q.append((nbr, node))
                    visited[nbr] = 1
                elif nbr != parent:
                    return True

        return False

    for i in range(V):
        if visited[i] != 1:
            if detectCycleBfs(i):
                return True

    return False


def isCycle(self, V: int, adj: List[List[int]]) -> bool:
    # Code here
    visited = [0]*(V)

    def detectCycleDfs(val, par):

        visited[val] = 1
        for nbr in adj[val]:
            if visited[nbr] != 1:
                if detectCycleDfs(nbr, val):
                    return True
            elif nbr != par:
                return True

        return False

    for i in range(V):
        if visited[i] != 1:
            if detectCycleDfs(i, -1):
                return True

    return False
