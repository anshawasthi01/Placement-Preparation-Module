# https://www.codingninjas.com/studio/problems/stack-implementation-using-array_3210209?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

from os import *

from sys import *

from collections import *

from math import *

 

# Stack class.

class Stack:

    

    def __init__(self, capacity: int):

        # Write your code here.

        self._stack = [0]*capacity

        self._top = 0

        self._size = capacity

 

    def push(self, num: int) -> None:

        if self._top >= self._size:

            return -1

        else:

            self._stack[self._top] = num

            self._top +=1

            return 1

 

    def pop(self) -> int:

        if self._top == 0:

            return -1

        else:

            self._top-=1

            return self._stack[self._top]

 

    def top(self) -> int:

        if self._top == 0:

            return -1

        else:

            return self._stack[self._top-1]

    

    def isEmpty(self) -> int:

        if self._top == 0:

            return 1

        else:

            return 0

    

    def isFull(self) -> int:

        # Write your code here.

        if self._top == self._size+1:

            return 1

        else:

            return 0

        pass