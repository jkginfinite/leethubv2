class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums),reverse=True)
        print(nums)
        if len(nums)>=3:
            return list(nums)[2]
        return max(nums)