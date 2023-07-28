# https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

from heapq import heapify, heappush, heappop

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        deadline_profit_map = {}
        max_time = 0
        for job in Jobs:
            max_time = max(max_time, job.deadline)
            if job.deadline in deadline_profit_map.keys():
                deadline_profit_map[job.deadline].append(job.profit)
            else:
                deadline_profit_map[job.deadline] = [job.profit]
    
        heap = []
        heapify(heap)
        tot_profit = 0
        count = 0
        for k in range(max_time, 0, -1):
            if k in deadline_profit_map.keys():
                for profit in deadline_profit_map[k]:
                    heappush(heap, -profit)
            if len(heap) != 0:
                tot_profit = tot_profit - heappop(heap)
                count += 1
        return [count, tot_profit]