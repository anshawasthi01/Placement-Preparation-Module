# https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    def topView(self,root):
        if root is None:
            return []
    
        node_dict = {}
        min_hd = max_hd = 0
    
        def traverse(node, hd, level):
            nonlocal node_dict, min_hd, max_hd
        
            if node is None:
                return
        
            if hd not in node_dict or level < node_dict[hd][1]:
                node_dict[hd] = (node.data, level)
        
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)
        
            traverse(node.left, hd - 1, level + 1)
            traverse(node.right, hd + 1, level + 1)
    
        traverse(root, 0, 0)
    
        top_view = [node_dict[hd][0] for hd in range(min_hd, max_hd + 1)]
        return top_view