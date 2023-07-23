# https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'

def inorder(root,ans):
    if root:
        inorder(root.left,ans)
        ans.append(root.data)
        inorder(root.right,ans)

class Solution:
    def kthLargest(self,root, k):
        #your code here
        ans = []
        inorder(root,ans)
        return ans[len(ans)-k]