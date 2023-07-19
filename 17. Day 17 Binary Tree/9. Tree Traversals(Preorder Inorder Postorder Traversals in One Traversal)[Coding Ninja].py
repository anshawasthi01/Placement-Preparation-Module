'''
    Time Complexity  : O(N)
    Space Complexity : O(N)

    Where 'N' is the total number of nodes in the binary tree.
'''

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

# Use result to store traversal of nodes.
result = []

def inOrder(node):
    # Base case.
    if (node == None):
        return

    # Visit left subtree.
    inOrder(node.left)
    # Add data of node to result.
    result[0].append(node.data)
    # Visit right subtree.
    inOrder(node.right)


def preOrder(node):
    # Base case.
    if (node == None):
        return
    
    # Add data of node to result.
    result[1].append(node.data)
    # Visit left subtree.
    preOrder(node.left)
    # Visit right subtree.
    preOrder(node.right)

def postOrder(node):
    # Base case.
    if (node == None):
        return

    # Visit left subtree.
    postOrder(node.left)
    # Visit right subtree.
    postOrder(node.right)
    # Add data of node to result.
    result[2].append(node.data)


def getTreeTraversal(root):
    global result  
    result.clear()
    result = [[],[],[]]
    # Call function to get inOrder Traversal.
    inOrder(root)
    # Call function to get preOrder Traversal.
    preOrder(root)
    # Call function to get postOrder Traversal.
    postOrder(root)

    # Return all 3 tree traversals.
    return result
# 

from os import *
from sys import *
from collections import *
from math import *

'''
    Time Complexity  : O(N)
    Space Complexity : O(N)

    Where 'N' is the total number of nodes in the binary tree.
'''

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

# Use result to store traversal of nodes.
result = []

def inOrder(node):
    # Base case.
    if (node == None):
        return

    # Visit left subtree.
    inOrder(node.left)
    # Add data of node to result.
    result[0].append(node.data)
    # Visit right subtree.
    inOrder(node.right)


def preOrder(node):
    # Base case.
    if (node == None):
        return
    
    # Add data of node to result.
    result[1].append(node.data)
    # Visit left subtree.
    preOrder(node.left)
    # Visit right subtree.
    preOrder(node.right)

def postOrder(node):
    # Base case.
    if (node == None):
        return

    # Visit left subtree.
    postOrder(node.left)
    # Visit right subtree.
    postOrder(node.right)
    # Add data of node to result.
    result[2].append(node.data)


def getTreeTraversal(root):
    global result  
    result.clear()
    result = [[],[],[]]
    # Call function to get inOrder Traversal.
    inOrder(root)
    # Call function to get preOrder Traversal.
    preOrder(root)
    # Call function to get postOrder Traversal.
    postOrder(root)

    # Return all 3 tree traversals.
    return result
