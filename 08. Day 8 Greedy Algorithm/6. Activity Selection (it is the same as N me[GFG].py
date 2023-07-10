# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/

#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        meeting=[(start[i],end[i]) for i in range(n)]
        
        meeting.sort(key=lambda a:a[1])
        
        count=1
        ansEnd=meeting[0][1]
        
        for i in range(1,n):
            if meeting[i][0]>ansEnd:
                count+=1
                ansEnd=meeting[i][1]
        return count