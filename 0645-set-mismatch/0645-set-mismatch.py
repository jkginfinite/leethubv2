class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = n*(n+1)//2
        s = n*(n+1)//2
        missing = s - sum(set(nums))
        duplicate = sum(nums)+missing-s
        return [duplicate,missing]