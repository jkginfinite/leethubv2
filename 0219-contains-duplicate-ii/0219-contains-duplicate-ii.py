class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_nums = {}
        for i,num in enumerate(nums):
            if num in seen_nums:
                if abs(seen_nums[num]-i)<=k:
                    return True
            seen_nums[num]=i
        return False