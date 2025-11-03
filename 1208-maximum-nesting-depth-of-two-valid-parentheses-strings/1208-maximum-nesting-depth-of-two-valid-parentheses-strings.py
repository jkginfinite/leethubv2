class Solution:
    def maxDepthAfterSplit(self, s: str) -> List[int]:
        groups = []
        d = 0
        for c in s:
            open = c == '('
            if open:
                d+=1
            groups.append(d%2)
            if not open:
                d-=1
        return groups