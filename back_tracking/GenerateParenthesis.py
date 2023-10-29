def generateParenthesis( n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []

    def dfs(s, left, right):
        if left == n == right:
            # 终止条件是括号数都是n
            res.append(s)
            return
        if right <= left <= n:
            # 如果左边的括号数大于右边的括号数且小于n则可以继续递归
            # 只要满足上述条件就一定还有分支有解
            dfs(s + '(', left+1, right)
            dfs(s + ')', left, right + 1)
    dfs('', 0, 0)
    return res


if __name__ == '__main__':
    print(generateParenthesis(n=3))
