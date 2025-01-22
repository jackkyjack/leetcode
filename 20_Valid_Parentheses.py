class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        
        dicti = {")": "(", "]": "[", "}": "{"}
        stack = []

        for paren in s:
            if paren in dicti:
                if stack and stack[-1] == dicti[paren]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(paren)
        
        if not stack:
            return True
        return False