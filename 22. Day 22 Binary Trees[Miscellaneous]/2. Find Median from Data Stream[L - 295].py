# https://leetcode.com/problems/find-median-from-data-stream/description/

from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        # max heap
        self.left = SortedList()
        
        # min heap
        self.right = SortedList()
        

    def addNum(self, num: int) -> None:
        self.left.add(num)
        
        if len(self.left) > len(self.right):
            v = self.left.pop(-1)
            self.right.add(v)
            
        else:
            if len(self.left) > 0 and self.left[-1] > self.right[0]:
                v = self.left.pop(-1)
                self.right.add(v)
                
                v = self.right.pop(0)
                self.left.add(v)

        
    def findMedian(self) -> float:
        if (len(self.left)+len(self.right))%2==0:
            return(self.left[-1]+self.right[0])/2
        else:
            return self.right[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()