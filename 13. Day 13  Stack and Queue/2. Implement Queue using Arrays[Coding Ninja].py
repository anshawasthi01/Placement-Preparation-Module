# https://www.codingninjas.com/studio/problems/implement-queue-using-arrays_8390825?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

class Queue:
    def __init__(self):
        self.size = 1000001
        self.arr = [None] * self.size
        self.front = 0
        self.rear = 0

    def enqueue(self, e):
        self.arr[self.rear] = e
        self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            return -1

        ans = self.arr[self.front]
        self.arr[self.front] = None
        self.front += 1

        if self.front == self.rear:
            self.front = self.rear = 0

        return ans
