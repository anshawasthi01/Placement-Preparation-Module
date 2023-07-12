# https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1#User function Template for python3

class Solution:
    def findPath(self, m, n):
        visited= [[0 for _ in range(n)] for _ in range(n)]
        ans=[]
        string=""
        if m[0][0]==1:
            self.solve(0,0,string,ans,m,n,visited)
        return ans
    
    def solve(self,row,col,string,ans,m,n,visited):
        if row==n-1 and col==n-1:
            ans.append(string)
            return
        
        ##downward
        
        if (row+1)<n and visited[row+1][col]==0 and m[row+1][col]==1:
            visited[row][col]=1
            self.solve(row+1,col,string+'D',ans,m,n,visited)
            visited[row][col]=0
            
        #Left
        if (col-1)>=0 and visited[row][col-1]==0 and m[row][col-1]==1:
            visited[row][col]=1
            self.solve(row,col-1,string+'L',ans,m,n,visited)
            visited[row][col]=0
        
        #Right    
        if (col+1)<n and visited[row][col+1]==0 and m[row][col+1]==1:
            visited[row][col]=1
            self.solve(row,col+1,string+'R',ans,m,n,visited)
            visited[row][col]=0
        
        #Upper    
        if (row-1)>=0 and visited[row-1][col]==0 and m[row-1][col]==1:
            visited[row][col]=1
            self.solve(row-1,col,string+'U',ans,m,n,visited)
            visited[row][col]=0