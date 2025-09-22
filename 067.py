class Solution(object):
    def addBinary(self, a, b):
        num1 = int(a, 2)
        num2 = int(b, 2)

        res = num1 + num2
        ans = bin(res)
        return ans[2:]