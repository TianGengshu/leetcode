class Solution:
    def merge(self, nums1, m: int, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
            
        p1 = m-1
        p2 = n-1
        p = len(nums1)-1
        

        while p1 >=0 and p2 >=0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
 
                p1-=1
            else:
                nums1[p] = nums2[p2]
                p2 -=1

            p -=1

        if p2 >=0:
            nums1[:p2+1] = nums2[:p2+1]
        return nums1

if __name__ == "__main__":
    s = Solution()
    print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))