class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        results = []
        last = None
        stack = heights
        while stack:
            position = len(stack)-1
            val = stack.pop()
            if not last:
                results.append(position)
                last = val
            else:
                if val>last:
                    results.append(position)
                last = max(last,val)
        return results[::-1]
        