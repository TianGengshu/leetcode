class Solution:

    def twoSum(self, nums, target: int) :
        if not nums:
            return None
        
        cache = {}
        for i in range(len(nums)):
            if nums[i] in cache:
                return[i,cache[nums[i]]]

            cache[target-nums[i]] = i
        return None 

            
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15],9))
