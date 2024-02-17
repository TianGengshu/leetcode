class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        merged = []
        while nums1 or nums2:
            if not nums1:
                merged.extend(nums2)
                break
            if not nums2:
                merged.extend(nums1)
                break
            
            if nums1[0] < nums2[0]:
                merged.append(nums1[0])
                nums1.pop(0)
            else:
                merged.append(nums2[0])
                nums2.pop(0)

        # return median from merged list
        print('merged')
        print(merged)

        if not merged:
            return 0

        n = len(merged)
        if n % 2 == 0:
            return (merged[int(n/2)] + merged[int(n/2)-1]) / 2
        else:
            return merged[int((n-1)/2)]


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4, 5]

    nums1 = [1, 3]
    nums2 = [2, 4]

    nums1 = []
    nums2 = [2, 4]

    nums1 = []
    nums2 = []
    print(Solution().findMedianSortedArrays(nums1, nums2))
