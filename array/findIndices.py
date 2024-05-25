from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for i in range(len(nums) - indexDifference):
            for j in range(i + indexDifference, len(nums)):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]


if __name__ == "__main__":
    s = Solution()
    print(s.findIndices([5, 1, 4, 1], 2, 4))
    print(s.findIndices([2,1], 0, 0))
    print(s.findIndices([1,2,3], 2, 4))