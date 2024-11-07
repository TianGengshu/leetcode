from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        current_low = 99999

        for price in prices:
            if price < current_low:
                current_low = price

            current_profit = price - current_low
            if current_profit > profit:
                profit = current_profit
        return profit


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5

    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    print(True)

# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?envType=problem-list-v2&envId=dynamic-programming