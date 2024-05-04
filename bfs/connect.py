# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/ 
# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # queue = deque([root])
        if not root:
            return None
        queue = [root]

        while queue:
            element_count = len(queue)
            print(element_count)
            for i in range(element_count):
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)

                # fix
                if i == element_count-1:
                    queue[i].next = None
                else:
                    queue[i].next = queue[i+1]

            # clear nodes in this level
            queue = queue[element_count:]
        
        return root
