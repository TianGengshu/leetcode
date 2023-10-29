class Solution:
    def permute(self, nums) :
        res = []
        if not nums:
            return []

        def backtracking(l, idx):
            # recursion return
            # if state(in this case l) satisfy condition , save
            if len(l) == len(nums):
                res.append(l.copy())
                return

            for i in range(len(nums)):
                # if nums in this index already seen, pass this iteration
                if nums[i] in l:
                    continue
                l.append(nums[i])
                backtracking(l, i)
                l.pop()

        backtracking([], 0)

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2]))