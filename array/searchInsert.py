class Solution:
    def searchInsert(self, nums, target) :

        lo,hi = 0,len(nums) -1

        while lo<=hi:
            mid = lo+int((hi-lo)/2)
            if nums[mid] == target:
                return mid
            if nums[mid]<target:
                lo = mid+1
            else:
                hi = mid-1
        return min(lo,hi) + 1 


if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1,3,5,6],5))
    print(s.searchInsert([1,3,5,6],0))
    print(s.searchInsert([1,3,5,6],2))
    print(s.searchInsert([1,3,5,6],7))
    print(s.searchInsert([1],0))