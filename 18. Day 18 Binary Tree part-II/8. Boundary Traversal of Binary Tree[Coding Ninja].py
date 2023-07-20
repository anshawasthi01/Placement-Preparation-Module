# https://www.codingninjas.com/studio/problems/boundary-traversal-of-binary-tree_790725?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of nodes in the Binary Tree.
'''

from queue import Queue

# Binary tree node class for reference.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def leftBoundary(root, ans):
    if(root == None or (root.left == None and root.right == None)):
        return

    ans.append(root.data)

    if(root.left != None):
        leftBoundary(root.left, ans)
    else:
        leftBoundary(root.right, ans)


def rightBoundary(root, ans):
    if(root == None or (root.left == None and root.right == None)):
        return

    if(root.right != None):
        rightBoundary(root.right, ans)
    else:
        rightBoundary(root.left, ans)

    ans.append(root.data)


def leafNodes(root, ans):
    if(root == None):
        return

    if(root.left == None and root.right == None):
        ans.append(root.data)
        return

    leafNodes(root.left, ans)
    leafNodes(root.right, ans)

# Functions to traverse on each part.
def traverseBoundary(root):
    # Write your code here.
    ans = []

    if(root == None):
        return ans

    ans.append(root.data)

    # Traverse left boundary.
    leftBoundary(root.left, ans)

    # Traverse for leaf nodes.
    leafNodes(root.left, ans)
    leafNodes(root.right, ans)

    # Traverse right boundary.
    rightBoundary(root.right, ans)

    return ans
