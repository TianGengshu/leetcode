class Solution:
    def combine(self, n: int, k: int) :
        nums = range(1,n+1)

        res = []

        def back_tracking(l):
            if len(l) == k:
                res.append(l.copy())  # if we have k elements , save the result and return
                return

            for n in nums:
                if n in l:
                    continue

                # avoid case like [1,2],[2,1], right element must > left element,
                if l and n<l[-1]:
                    continue

                l.append(n)
                back_tracking(l)
                l.pop()

        back_tracking([])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4,2))
