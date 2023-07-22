# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        # Start with the root node
        queue = [root]
        
        while queue:
            # Get the number of nodes in the current level
            size = len(queue)
            
            # Traverse through the nodes in the current level
            for i in range(size):
                # Get the first node from the queue
                node = queue.pop(0)
                
                # If it's not the last node in the level, set its next to the next node in the queue
                if i < size - 1:
                    node.next = queue[0]
                
                # Add the node's children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        # Return the root node
        return root