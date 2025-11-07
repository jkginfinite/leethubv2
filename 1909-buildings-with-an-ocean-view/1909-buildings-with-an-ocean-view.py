class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        results = []
        last = 0
        stack = heights
        while stack:
            position = len(stack)-1
            val = stack.pop()
            if val>last:
                results.append(position)
            last = max(last,val)
        return results[::-1]
        