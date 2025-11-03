class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        depth = 0
        max_depth = 0
        for c in s:
            if c in ['(',')']:
                max_depth = max(depth,max_depth)
                if c=='(':
                    stack.append(c)
                    depth+=1
                if c==')' and stack[-1]=='(':
                    stack.pop()
                    depth-=1
        return max_depth