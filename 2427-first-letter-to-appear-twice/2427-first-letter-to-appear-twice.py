class Solution:
    def repeatedCharacter(self, s: str) -> str:
        queue = list(s)
        d = {}
        while queue:
            l = queue.pop(0)
            if l not in d:
                d[l]=1
            else:
                return l        