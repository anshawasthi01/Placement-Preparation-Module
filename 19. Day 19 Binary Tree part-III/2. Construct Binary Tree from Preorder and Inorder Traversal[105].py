# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build(preorder,inorder,ist,ien,d):
            if ist>ien or len(preorder)==0:
                return None
            ele = preorder.pop(0)
            root = TreeNode(ele)
            idx = d[ele]
            root.left = build(preorder,inorder,ist,idx-1,d)
            root.right = build(preorder,inorder,idx+1,ien,d)
            return root


        d,n = {},len(preorder)
        for i in range(len(inorder)):
            d[inorder[i]] = i
        root = build(preorder,inorder,0,n-1,d)
        return root