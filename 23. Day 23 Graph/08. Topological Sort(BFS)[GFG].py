# https://practice.geeksforgeeks.org/problems/topological-sort/1

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):

       

        def dfs(node):

            if visited[node] == 1:

                return

            visited[node] = 1

            for vertex in adj[node]:

                    dfs(vertex)

            stack.append(node)

           

        visited = [0]*V

        stack = []

        for i in range(V):

            if visited[i] == 0:

                dfs(i)

        return stack[::-1]