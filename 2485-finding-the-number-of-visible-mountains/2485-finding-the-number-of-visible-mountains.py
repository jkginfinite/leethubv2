class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        c = collections.Counter()

        for x,y in peaks:
            c[(x,y)]+=1
        peaks = sorted(c.keys())
        if not peaks:
            return 0
        
        def within(pa,pb):
            x1,y1 = pa
            x2,y2 = pb
            b1 = y1-x1
            b2 = y1+x1
            return y2<=x2+b1 and y2<=b2-x2

        n = len(peaks)
        stack = [peaks[0]]

        for x,y in peaks[1:]:
            while stack and within([x,y],stack[-1]):
                stack.pop()
            if not stack or not within(stack[-1],[x,y]):
                stack.append((x,y))
        return len([p for p in stack if c[p]==1])