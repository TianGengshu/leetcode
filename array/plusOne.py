class Solution:
    def plusOne(self, digits ):
        res_list = []
        i = len(digits) -1
        carry = 1
        while i >= 0 :
            if digits[i] == 9 and carry ==1:
                carry = 1
                res_list = [0] + res_list
            else:
                res_list = [digits[i] + carry] + res_list
                carry = 0
            i-=1
        if carry ==1:
            res_list = [1] + res_list
        return res_list

        
if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([1,2,3,4]))
    print(s.plusOne([9,9,9,9]))
    print(s.plusOne([1,9,9,9,9]))
    print(s.plusOne([1,0,0,9,9]))