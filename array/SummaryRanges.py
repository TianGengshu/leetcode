class Solution:
    def summaryRanges(self, nums):
        i = 0
        res_list =[]
        while i < len(nums):
            j = i 
            while j+1 < len(nums) and nums[j+1] == nums[j]+1:
                j+=1

           
            res_list.append([nums[i],nums[j]])

            i = j+1
        def format(l):
            if l[0] == l[1]:
                return str(l[0])
            else:
                return str(l[0]) + "->" + str(l[1])
        res_list = [format(i) for i in res_list]
        return res_list

'''
[0,1,2,4,5,7]
 i   j

'''
if __name__ == "__main__":
    s = Solution()
    print(s.summaryRanges([0,1,2,4,5,7]))


'''
      distance  avg-people competitiveness quality for-dunk 
tt
gqm
dd
xx 
fz
szkj 
sjz
slh 
ltzh



'''