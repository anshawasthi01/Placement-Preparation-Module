# https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/0?fbclid=IwAR2_lL0T84DnciLyzMTQuVTMBOi82nTWNLuXjUgahnrtBgkphKiYk6xcyJU

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        
        dist = [float('inf') for i in range(V)]
        dist[S] = 0
        for i in range(V-1):
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[v]>w+dist[u] :
                    dist[v] = min(dist[v], dist[u] + w)
                    
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return [-1]
                
        for i in range(len(dist)):
            if dist[i] == float('inf'):
                dist[i] = 100000000
        return dist