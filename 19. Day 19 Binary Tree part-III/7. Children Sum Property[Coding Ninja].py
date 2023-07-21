# https://www.codingninjas.com/studio/problems/children-sum-property_8357239?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

'''
    Following is the class structure of the Node class:

    class Node:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
'''
'''
    Time Complexity: O( N )
    Space Complexity: O( N )

    where â€˜Nâ€™ is the number of nodes in the binary tree. 
'''

def isParentSum(root):
    # Base case: If the root is NULL or it is a leaf node, it satisfies the Parent Sum property.
    if root is None or (root.left is None and root.right is None):
        return True
    
    # Subtract the values of the left and right child from the current node's value.
    if root.left:
        root.data -= root.left.data
    
    if root.right:
        root.data -= root.right.data
    
    # Check if the current node's value is equal to the sum of its children's values.
    if root.data == 0:

        # Recursively check the Parent Sum property for the left and right subtrees.
        return isParentSum(root.left) and isParentSum(root.right)
    
    # If the current node's value is not equal to the sum of its children's values, it does not satisfy the Parent Sum property.
    return False
