class Solution:
    def sortedSquares(self, nums) :
        pass
        n = len(nums)
        res = [0]*n
        lo,hi = 0,n-1
        while lo<=hi:
            if nums[lo]*nums[lo] < nums[hi]*nums[hi]:
                res[n-1] = nums[hi]*nums[hi]
                hi-=1
            else:
                res[n-1] = nums[lo]*nums[lo]
                lo+=1
            n-=1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.sortedSquares([-7,-3,2,3,11]))
    print(s.sortedSquares([-4,-1,0,3,10]))
