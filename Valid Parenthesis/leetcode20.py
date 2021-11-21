class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(' : ')', '{' : '}', '[' : ']'}
        keys = list(dict.keys())
        values = list(dict.values())
        stack = []
        for i in range(len(s)):
            if s[i] in keys:
                stack.append(s[i])
            elif len(stack) > 0:
                if s[i] in values and stack[-1] == keys[values.index(s[i])]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return stack == []
