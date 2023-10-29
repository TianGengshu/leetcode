# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) :
        output = []
        self.dfs(root,output)
        min_abs = float('inf')

        for i in range(1,len(output)):
            min_abs = min(min_abs,output[i] - output[i-1])
        
        return min_abs

    def dfs(self,root,output):
        if root is None :
            return 
        
        self.dfs(root.left,output)
        output.append(root.val)
        self.dfs(root.right,output)

