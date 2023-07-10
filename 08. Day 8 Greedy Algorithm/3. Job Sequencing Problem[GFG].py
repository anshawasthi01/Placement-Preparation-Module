# https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#

#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        # code here
        Jobs.sort(key=lambda x:x.profit,reverse=True)
        time=0
        profit=0
        vis=[0]*n
        for i in Jobs:
            for j in range(i.deadline-1,-1,-1):
                if vis[j]==0:
                    vis[j]=1
                    time+=1
                    profit+=i.profit
                    break
        return time,profit