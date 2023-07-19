# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root_: TreeNode | None) -> list[int]:
        def inorder(root: TreeNode | None) -> Iterable[int]:
            yield from chain(inorder(root.left), (root,), inorder(root.right)) if root else tuple()
        
        return [node.val for node in inorder(root_)]


