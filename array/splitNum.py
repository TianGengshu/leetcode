class Solution:
    def splitNum(self, num: int) -> int:
        min_val = 99999
        for flag in range(len(str(num))):
            num1 = int(str(num)[:flag])
            num2 = int(str(num)[flag:])
            if num1+num2 < min_val:
                min_val = num1+num2
        return min_val



