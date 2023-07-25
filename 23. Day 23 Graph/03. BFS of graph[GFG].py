# https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        q = deque()
        bfs = []
        h = {}
        j = 0
        q.append(j)
        while q:
            visited.append(q.popleft())
            for k in adj[visited[j]]:
                if k in h:
                    h[k] += 1
                else:
                    q.append(k)
                    h[k] = 0
            j += 1
        return bfs