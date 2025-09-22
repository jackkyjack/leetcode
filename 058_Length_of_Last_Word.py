class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        if not s:
            return 0
        words = s.split(" ")
        return len(words[-1])