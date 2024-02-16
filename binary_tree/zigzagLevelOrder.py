from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []

        queue = [root]
        flag = True
        result = []

        while queue:
            r = deque([])
            # print([i.val for i in queue])
            for _ in range(len(queue)):
                elem = queue[0]
                queue = queue[1:]

                if flag:
                    r.append(elem.val)
                else:
                    r.appendleft(elem.val)

                if elem.left:
                    queue.append(elem.left)

                if elem.right:
                    queue.append(elem.right)

            flag = not flag
            result.append(list(r))

        return result


if __name__ == '__main__':
    s = Solution()
