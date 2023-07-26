# https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        mst = []
        vis = [0]*V
        pq = []
        sm = 0
        # wt , node
        heapq.heappush(pq,(0,0))
        while len(pq)!=0:
            wt,node = heapq.heappop(pq)
            if vis[node] == 1:
                continue
            vis[node] = 1
            sm += wt
            for adjNode,edw in adj[node]:
                if not vis[adjNode]:
                    heapq.heappush(pq,(edw,adjNode))
        return sm