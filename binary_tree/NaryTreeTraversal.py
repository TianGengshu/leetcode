"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node'):
        if not root:
            return []

        queue = [root]

        result = []

        while queue:

            level = []
            for _ in range(len(queue)):
                item = queue.pop(0)
                level.append(item.val)

                if item.children:
                    for c in item.children:
                        queue.append(c)

            result.append(level)
            

        return result