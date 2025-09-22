class Solution(object):
    def mySqrt(self, x):
        num = 0
        while((num*num) <= x):
            num+=1
        return num-1