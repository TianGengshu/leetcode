# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None or q is None:
            return p == q 
        
        if p.val != q.val:
            return False
            


        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        

class Solution_BFS:
    def isSameTree(self, p:TreeNode, q:TreeNode) -> bool:
        q1 = [p]
        q2 = [q]

        while q1 and q2:

            elem1 = q1[0]
            q1 = q1[1:]
            elem2 = q2[0]
            q2 = q2[1:]

            if elem1.val != elem2.val:
                return False 

            q1.append(elem1.left)
            
            q2.append(elem1.left)

            q1.append(elem1.right)
            
            q2.append(elem2.right)


        return True