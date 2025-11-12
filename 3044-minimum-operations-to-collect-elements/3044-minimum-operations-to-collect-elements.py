class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sett = set()
        i = len(nums)-1

        while len(sett)<k:
            if nums[i]<=k:
                sett.add(nums[i])
            i-=1
        return len(nums)-i-1
        