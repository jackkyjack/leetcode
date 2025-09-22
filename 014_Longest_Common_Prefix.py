class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        txt = strs[0]
        for i in strs[1:]:
            while not i.startswith(txt):
                txt = txt[:-1]
        return txt
