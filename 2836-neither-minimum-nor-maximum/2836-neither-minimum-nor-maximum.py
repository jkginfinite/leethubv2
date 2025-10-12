class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        edges = [min(nums),max(nums)]
        for i in nums:
            if i not in edges:
                return i
        return -1