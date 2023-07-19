# https://www.codingninjas.com/studio/problems/preorder-traversal_3838888?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

'''
	 
	 Following is the Binary Tree node structure:
	 
	 class TreeNode:
	     def __init__(self, data=0, left=None, right=None):
	         self.data = data
	         self.left = left
	         self.right = right
'''

def preOrderHelper(root, answer):
    # Base case.
    if root == None:
        return

    # Add data of node to answer.
    answer.append(root.data)
    
    # Visit left subtree.
    preOrderHelper(root.left, answer)

    # Visit right subtree.
    preOrderHelper(root.right, answer)


def getPreOrderTraversal(root):
    # Use answer to store traversal of nodes.
    answer = []

    # Call preOrderHelper function and store preOrder traversal in answer array.
    preOrderHelper(root, answer)

    # Return answer.
    return answer
