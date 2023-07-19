# https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

class Solution:
    def bottomView(self, root):
        if root is None:
            return []
        
        q = [(root, 0)]
        node_dict = {}
    
        while q:
            node, hd = q.pop(0)
            node_dict[hd] = node.data
        
            if node.left:
                q.append((node.left, hd - 1))
            
            if node.right:
                q.append((node.right, hd + 1))
            
        bottom_view = [node_dict[hd] for hd in sorted(node_dict)]
        return bottom_view