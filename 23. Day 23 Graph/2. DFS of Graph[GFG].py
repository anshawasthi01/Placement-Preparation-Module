# https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # recur function for dfs
        def recur(adj, s, visited, ans):
            visited[s] = 1
            ans.append(s)
            for j in adj[s]:
                if visited[j] == 0:
                    recur(adj, j, visited,ans)
        ans = []
        visited = [0]*V
        # calling dfs for every vertex
        for i in range(V):
            if (visited[i] == 0):
                recur(adj, i, visited, ans)
        return ans