class Solution:
    def findPath(self, m, n):
        res = []
        curr = []
        # code here

        def pathdfs(i, j, c):
            if i < 0 or j < 0 or i >= n or j >= n:
                return

            if i == n-1 and j == n-1 and m[i][j] == 1:
                curr.append(c)
                res.append("".join(curr))
                curr.pop()
                return

            if m[i][j] == 1:
                curr.append(c)
                m[i][j] = 0
                pathdfs(i, j+1, 'R')
                pathdfs(i+1, j, 'D')
                pathdfs(i, j-1, 'L')
                pathdfs(i-1, j, 'U')
                m[i][j] = 1
                curr.pop()

            return

        pathdfs(0, 0, '')
        return res
