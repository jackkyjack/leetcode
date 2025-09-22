class Solution(object):
    def plusOne(self, digits):
        nums = 0
        for i in range(len(digits)):
            nums = nums*10 + digits[i]
        nums+=1
        str_num = str(nums)
        res = []
        for i in str_num:
            res.append(int(i))
        return res