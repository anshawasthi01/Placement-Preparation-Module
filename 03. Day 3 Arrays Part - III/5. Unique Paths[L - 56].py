# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0]*m for i in range(n)]
        for c in range(m):
            paths[n-1][c] = 1
        for r in range(n):
            paths[r][m-1] = 1
        for r in range(n-2, -1, -1):
            for c in range(m-2, -1, -1):
                paths[r][c] = paths[r][c+1] + paths[r+1][c]
            
        return paths[0][0]