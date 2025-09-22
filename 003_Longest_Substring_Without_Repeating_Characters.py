class Solution(object):
    def lengthOfLongestSubstring(self, s):
        m=0
        for i in range(len(s)):
            temp=[]
            j=i
            while j<len(s) and s[j] not in temp:
                temp+=[s[j]]
                j+=1
            if len(temp)>m:
                m = len(temp)
        return m
    
s = "pwwkew"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))