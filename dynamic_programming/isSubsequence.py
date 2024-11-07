class Solution_SimpleQueue:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return False
        queue = [char for char in s]
        for char in t:
            if char == queue[0]:
                queue.pop(0)

        return queue == []


class Solution_DP:
    def isSubsequence(self, s: str, t: str) -> bool:
        pass


class Solution_TwoPointers:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        spointer = 0
        for tpointer in range(len(t)):
            if spointer < len(s) and t[tpointer] == s[spointer]:
                spointer += 1
        return spointer == len(s)


if __name__ == "__main__":
    s = Solution_SimpleQueue()
    # s = Solution_TwoPointers()
    assert s.isSubsequence(s="abc", t="ahbgdc") is True
    assert s.isSubsequence(s="", t="ahbgdc") is True
    assert s.isSubsequence(s="b", t="abc") is True
    print('pass')

# https://leetcode.cn/problems/is-subsequence/?envType=problem-list-v2&envId=dynamic-programming
