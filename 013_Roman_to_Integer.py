class Solution(object):
    def romanToInt(self, s):
        dicts = {"I" : 1,
                "V" : 5,
                "X" : 10,
                "L" : 50,
                "C" : 100,
                "D" : 500,
                "M" : 1000}
        sum = 0
        while s != "":
            if len(s)>1 and dicts[s[1]] > dicts[s[0]]:
                sum += dicts[s[1]] - dicts[s[0]]
                s = s[2:]
            else:
                sum += dicts[s[0]]
                s = s[1:]

        return sum