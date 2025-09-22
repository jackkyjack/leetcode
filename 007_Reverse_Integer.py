class Solution(object):
    def reverse(self, x):
        num = abs(x)
        res = 0
        sign = 1 if x >= 0 else -1

        while num > 0:
            digit = num % 10
            res = res * 10 + digit
            num //= 10
        res *= sign

        return res if (-2)**31-1 <= res <= 2**31-1 else 0