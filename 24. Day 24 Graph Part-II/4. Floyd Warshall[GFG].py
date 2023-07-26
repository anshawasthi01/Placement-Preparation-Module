# https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1

class Solution:
    def shortest_distance(self, cost):
        n=len(cost)
        for i in range(n):
            for j in range(n):
                if cost[i][j] == -1:
                    cost[i][j] = float('inf')
                if i == j:
                    cost[i][j] = 0
                    
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if cost[i][via]+cost[via][j]<cost[i][j]:
                        cost[i][j]=cost[i][via]+cost[via][j]
        for i in range(n):
            for j in range(n):
                if cost[i][j] == float('inf'):
                    cost[i][j] = -1