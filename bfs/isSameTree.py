# https://leetcode.cn/problems/same-tree/
# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()

            # when a node has left/right but another doesn't
            if (not node1.left) ^ (not node2.left):   # if differnet
                return False

            if (not node1.right) ^ (not node2.right):
                return False

            if node1.val != node2.val:
                return False

            if node1.left:
                queue1.append(node1.left)
            
            if node2.left:
                queue2.append(node2.left)

            if node1.right:
                queue1.append(node1.right)
            
            if node2.right:
                queue2.append(node2.right)

        if queue1 or queue2:
            return False

        return True
            


