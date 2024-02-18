from types import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution_recursive:
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        def trav(node):
            if not node:
                return
            result.append(node.val)
            for child in node.children:
                trav(child)
        trav(root)
        return result


class Solution_iterative:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.children:
                stack.extend(reversed(node.children))
        return result
