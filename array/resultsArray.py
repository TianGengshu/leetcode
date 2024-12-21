from typing import List


class Solution_Two_Pointer_Exceed_Time:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums)-k+1):
            move = 1
            while move < k:
                if nums[i+move] - nums[i] != move:
                    res.append(-1)
                    move = -1
                    break

                move += 1
            if move == k:
                print('register')
                print(i, move)
                res.append(nums[i+move-1])

        print(res)
        return res


class Solution_DP:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        pass


if __name__ == "__main__":
    s = Solution_Two_Pointer_Exceed_Time()
    assert s.resultsArray([1, 2, 3, 4, 3, 2, 5], 3) == [3, 4, -1, -1, -1]
    assert s.resultsArray([2, 2, 2, 2, 2], 4) == [-1, -1]

    print('pass')
# https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-ii/?envType=daily-question&envId=2024-11-07

'''
1 2 3 4 3 2 5
i

'''