# https://www.codingninjas.com/studio/problems/all-root-to-leaf-paths-in-binary-tree._983599?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the class structure of the BinaryTreeNode class:

    class BinaryTreeNode:
        def __init__(self, data):

            self.data = data
            self.left = None
            self.right = None

'''

'''
    Time Complexity : O(N)
    Space Complexity : O(N)
    
    Where N is the number of nodes in the tree.
'''

def dfs(root, result, curr):

    # Base Case.
    if root is None:
        return

    # Current string consists of data at root node.
    if len(curr) == 0:
        curr += str(root.data)

    else:
        curr += " " + str(root.data)

    # If both child of root is NULL, then pushing the path in result array.
    if root.left is None and root.right is None:
        result.append(curr)

    # If left child is not NULL, traverse on the left side.
    dfs(root.left, result, curr)

    # If right child is not NULL, traverse on the right side.
    dfs(root.right, result, curr)

def allRootToLeaf(root):

    # It stores all the paths from root to leaf.
    result = list()

    # It is used for traversal.
    dfs(root, result, "")
    return result

