class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo ,hi = 0,n-1

        while lo<hi:
            mid = lo + int((hi-lo)/2)

            if isBadVersion(mid):
                hi = mid
            else:
                left = mid+1
        return lo
