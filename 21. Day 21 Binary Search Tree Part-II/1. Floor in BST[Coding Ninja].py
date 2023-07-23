# https://www.codingninjas.com/studio/problems/floor-from-bst_920457?source=youtube&campaign=Striver_Tree_Videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=Striver_Tree_Videos&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    Following is the TreeNode class structure

    class TreeNode:

        def __init__ (self, data):

            self.data = data
            self.left = None
            self.right = None
            
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''
    Time Complexity: O(N)
    Space Complexity: O(1)

    Where 'N' is the number of nodes in the given tree.
'''


def floorInBST(root, X):

    # Base Case
    if root is None:
        return -1

    # Find the floor in left sub tree
    leftFloor = floorInBST(root . left, X)

    # Find the floor in right sub tree
    rightFloor = floorInBST(root . right, X)

    # Let the answer be -1
    ans = -1

    # If right floor is less than 'X' and but greater then left floor
    if (leftFloor <= rightFloor and rightFloor <= X):
        ans = rightFloor

    # If left floor is less than 'X' and but greater then right floor
    if (leftFloor > rightFloor and leftFloor <= X):
        ans = leftFloor


    # If root . data is less than 'X' and greater than 'ans' then root value is more close to 'X'
    if (root.data > ans and root.data <= X):
        ans = root.data
        
    return ans



