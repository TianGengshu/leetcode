# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) :
        if not root:return []

        q =[root]
        result = []

        while q:
            r = []
            for i in range(len(q)):
                elem = q[0]
                q = q[1:]
                r.append(elem.val)

                if elem.left:q.append(elem.left)
                if elem.right:q.append(elem.right)
            
            result.append(r)

        return result



