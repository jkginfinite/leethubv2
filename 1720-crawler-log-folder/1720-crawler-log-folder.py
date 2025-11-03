class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for l in logs:
            if l=='./':
                #stack.pop()
                pass
            elif l=='../':
                if stack:
                    stack.pop()
            else:
                stack.append(l)
        return len(stack)