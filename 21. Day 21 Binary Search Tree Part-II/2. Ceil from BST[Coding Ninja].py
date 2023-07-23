# https://www.codingninjas.com/studio/problems/ceil-from-bst_920464?source=youtube&campaign=Striver_Tree_Videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=Striver_Tree_Videos&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the TreeNode class structure

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''

'''
    Time complexity: O(logN)
    Space complexity: O(logN)

    Where 'N' is the number of nodes of the tree
'''


def findCeil(node, x):
    # Initializing ceil value
    ceil = -1

    # Traverse till the node is not null
    while(node != None):

        # If node value equals key then return it
        if x == node.data:
            return node.data

        # Traverse right sub-tree
        if x > node.data:
            node = node.right

        # Traverse left sub-tree
        else:
            ceil = node.data
            node = node.left

    return ceil
