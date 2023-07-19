# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:        
        #Approach - Using Recursion
        a = []
        if not root:
            return 
        if root.left:
            a +=self. postorderTraversal(root.left)     
        if root.right:
            a += self.postorderTraversal(root.right)     
        a.append(root.val)
        return a
                
        