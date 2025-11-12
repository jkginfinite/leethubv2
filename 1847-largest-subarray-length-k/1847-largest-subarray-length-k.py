class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        n, i, j, d = len(nums), 0, 1, 0
        while j+k-1<n:
            if nums[i+d]==nums[j+d] and d<k:
                d+=1
                continue
            if nums[i+d]<nums[j+d]:
                i = max(i+d+1,j)
                j = i+1
            else:
                j = j+d+1
            d=0
        return nums[i:i+k]