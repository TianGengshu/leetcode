class Solution:
    def search(self, nums, target):
        lo,hi = 0,len(nums)-1
        while lo<= hi:
            # print("lo = {} hi = {}".format(lo,hi))

            mid = int((hi-lo)/2)+lo

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                lo = mid+1
            else:
                hi = mid-1
            
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([-1,0,3,5,9,12],-31))
    print(s.search([-1,0,3,5,9,12],12))
    print(s.search([-1,0,3,5,9,12],-1))

