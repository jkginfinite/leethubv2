class Solution(object):
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            else:
                if stack:
                    if stack[-1]==d[i]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(i)
        return not stack
