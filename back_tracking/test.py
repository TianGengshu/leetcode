class Solution:
    def f(self):
        l = []
        def add12(l):
            l.append([1,2])
            # return l
        add12(l)
        add12(l)
        return l
s = Solution()
print(s.f())