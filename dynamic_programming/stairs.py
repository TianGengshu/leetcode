class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)

        for i in range(n+1):
            if i == 0:
                dp[i] = 0
            elif i == 1:
                dp[i] = 1
                print(dp)
            elif i == 2:
                dp[i] = 2
            else:
                dp[i] = dp[i-1] + dp[i-2]
                print(dp)
        print(dp)
        return dp[-1]


class Solution_Memo:
    def climbStairs(self, n: int) -> int:
        mem = [0, 1, 2] + [0] * n
        return self.climbStairsmemo(n, mem)

    def climbStairsmemo(self, n: int, mem) -> int:
        if mem[n] > 0:
            return mem[n]
        if n <= 2:
            return n
        count = self.climbStairsmemo(n-1, mem) + self.climbStairsmemo(n-2, mem)
        mem[n] = count
        return count


class Solution_Mem:
    mem = [1, 2].extend([0] * 1000)

    def climbStairs(self, n: int) -> int:

        if self.mem[n] != 0:
            return self.mem[n]
        if n < 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)


# class Solution_Magic_Cache:

#     @cache
#     def climbStairs(self, n: int) -> int:
#         return n if n<2 else self.climbStairs(n-2)+self.climbStairs(n-1)


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(3))

# https://leetcode.cn/problems/climbing-stairs/description/?envType=problem-list-v2&envId=dynamic-programming