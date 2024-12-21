from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = int((right+left)/2)

            # if for a given element, it's different to both previous and after
            # or this is the last element and different to it's previous
            # this will be captured
            if mid == len(nums)-1 or nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]: # noqa
                return nums[mid]

            # normally in a given position, the element after even position must equals to this element # noqa
            # otherwise there must be abnormal element
            if mid % 2 == 0 and nums[mid+1] != nums[mid] or mid % 2 != 0 and nums[mid-1] != nums[mid]: # noqa 
                right = mid - 1
            else:
                left = mid+1


if __name__ == "__main__":
    s = Solution()
    assert s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
    print('pass 1 ')
    assert s.singleNonDuplicate([1, 1, 2]) == 2
    print('pass')
