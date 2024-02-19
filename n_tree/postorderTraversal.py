from types import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def trav(node):
            if not node:
                return 
            for child in node.children:
                trav(child)
            result.append(node.val)

        trav(root)
        return result

    def psotorder_iterative(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        traversed = set()
        while stack:
            node = stack[-1]
            if not node.children or node in traversed:
                result.append(node.val)
                stack.pop()
                continue

            stack.extend(reversed(node.children))
            traversed.add(node)

        return result
