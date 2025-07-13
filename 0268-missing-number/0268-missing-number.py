class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if sum(range(max(nums)+1))-sum(nums) in nums:
            return max(nums)+1
        return sum(range(max(nums)+1))-sum(nums)