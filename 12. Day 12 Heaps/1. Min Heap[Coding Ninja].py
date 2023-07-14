# https://www.codingninjas.com/studio/problems/min-heap_4691801?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0


from os import *
from sys import *
from collections import *
from math import *


# Left child of the node.

def left(k):

    return 2 * k + 1

 

# Right child of the node.

def right(k) -> int:

    return 2 * k + 2

 

# Returns the parent node.

def parent(k) -> int:

    return (k - 1) // 2

 

# Heapify the heap

def heapify(heap, k, size):

 

    # Find the left child of the node.

    l = left(k)

 

    # Find the right child of the node.

    r = right(k)

 

    # Find the smallest element between the current node and its children.

    # Check if the left child is smallest.

    smallest = k

    if l < size[0] and heap[l] < heap[k]:

        smallest = l

 

    # Check if the right node is smallest then the previous smallest.

    if r < size[0] and heap[r] < heap[smallest]:

        smallest = r

 

    # If the smallest element is not in the current node.

    # We have to heapify the Heap to take that element to the top.

    if smallest != k:

 

        # Swap the values of current node and the smallest node value.

        heap[k], heap[smallest] = heap[smallest], heap[k]

 

        # Call the heapify function on smallest value node which now contains the value of parent node.

        heapify(heap, smallest, size)

 

# Insert a val in the heap.

# Function contains heap array, val to inserted and the current size of the heap.

def insert(heap: [], val: int, size: []):

 

    # Insert the val at the end of the heap.

    heap[size[0]] = val

 

    # If There is nore than 1 node in the Heap.

    # MinHeapify the heap by checking the val at its parent node.

    # Also do it until the heap property is not satisfied.

    i = size[0]

    size[0] += 1

    while i != 0 and heap[parent(i)] > heap[i]:

 

        # Swap the value of current node with its parent.

        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]

 

        # Check that if the parent element of current element is satisfying the heap property.

        i = parent(i)

 

def extractMin(heap: [], size: []) -> int:

    # Check if the current node is the only node in the heap.

    if size[0] == 1:

        size[0] -= 1

        return heap[0]

 

    # Takeout the min value and remove it from the heap.

    val = heap[0]

 

    # Put last node on the top of heap.

    heap[0] = heap[size[0] - 1]

 

    # Decrease the size of heap as the minimum element is removed.

    size[0] -= 1

 

    # Heapify the heap to satisfy the heap property.

    heapify(heap, 0, size)

    return val

 

# Define minHeap function which take size of Queries and Queries as Input.

# Returns an array out outputs depending on the query.

def minHeap(n: int, q: [[]]) -> []:
    # Write your code frome here.

 

    # Size of the heap.

    size = [0]

    # Define a heap array to store elements.

    heap = [None] * n

 

    # Define an array which stores the min elements.

    ans = []

 

    # For each query in the array Q.

    for i in range(n):

 

        # If query is of type 1 then insert the value in the heap.

        # Else take min element from the heap and append it in the ans.

        if q[i][0] == 0:

            insert(heap, q[i][1], size)

        else:

            ans.append(extractMin(heap, size))

 

    # Return the ans array.

    return ans

