# https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    
    # code here
    ans=[]
    if root is None:
        return ans
    q=[]
    q.append(root)
    
    while q:
        
        l=[]
        for _ in range(len(q)):
            r=q.pop(0)
            l.append(r.data)
            if r.left:
                q.append(r.left)
            
            if r.right:
                q.append(r.right)
        ans.append(l[0]) 
    
    return ans