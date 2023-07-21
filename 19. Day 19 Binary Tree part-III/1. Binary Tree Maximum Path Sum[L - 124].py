# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        path = -10 ** 20

        # gives max path for this edge
        def traverse (node):
            if node is None:
                return 0

            # a path that goes through this node connecting left and right
            left = traverse(node.left)
            right = traverse(node.right)
            v = node.val + max(left,0) + max(right,0)

            nonlocal path
            path = max(path, v)

            return node.val + max(max(left, right), 0)

        traverse(root)
        return path