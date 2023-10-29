class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        pos = {}
        for i in range(len(nums)):
            if nums[i] in pos and i - pos[nums[i]] <= k :
                return True
            pos[nums[i]] = i
        return False
       
    

if __name__ == "__main__":
    s = Solution()
    print(s.containsNearbyDuplicate([1,2,3,1],3)) #t
    print(s.containsNearbyDuplicate([1,0,1,1],1)) #t
    print(s.containsNearbyDuplicate([1,2,3,1,2,3],2)) #f
    print(s.containsNearbyDuplicate([99,99],2)) # True
    print(s.containsNearbyDuplicate([99,98],2)) # False 
    print(s.containsNearbyDuplicate([2,2],3)) # True