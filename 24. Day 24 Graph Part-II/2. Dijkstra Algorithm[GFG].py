# https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

from queue import PriorityQueue

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        pq = PriorityQueue()
        dist = [float('inf')] * V
        # distance from source to source is zero
        dist[S] = 0
        pq.put((0,S))
        while not pq.empty():
            dis, node = pq.get()
            for v in adj[node]:
                # neighbour node stored at 0th index and weight at 1st index
                adjNode = v[0]
                edgeWeight = v[1]
                
                if dis + edgeWeight < dist[adjNode]:
                    dist[adjNode] = dis + edgeWeight
                    pq.put((dist[adjNode], adjNode))
        return dist