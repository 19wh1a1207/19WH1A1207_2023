//Not executed, still trying
class Solution:
    def minInsertions(self, s: str) -> int:
        left, res = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                if((i + 1) < len(s) and s[i + 1] == ')'):
                    if left > 0:
                        left -= 1
                        i += 1
                    else:
                        res += 1
                        i += 1
                else:
                    if left > 0:
                        left -= 1
                        res += 1
                    else:
                        res += 2
        res += (left * 2)
        return res            
