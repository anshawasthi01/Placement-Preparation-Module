# https://www.codingninjas.com/studio/problems/merge-k-sorted-arrays_975379?leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

import heapq
def mergeKSortedArrays(kArrays, k:int):
	# Write your code here.
	# kArrays is a list of 'k' lists.
	# Return a list.


    heap=[]

    final=[]

    for i in range(len(kArrays)):

        heapq.heappush(heap,(kArrays[i][0],i,0))

 

    while heap:

        ele,aIndex,eleIndex=heapq.heappop(heap)

        final.append(ele)

        if eleIndex+1<len(kArrays[aIndex]):

            heapq.heappush(heap,(kArrays[aIndex][eleIndex+1],aIndex,eleIndex+1))

 

    return final
