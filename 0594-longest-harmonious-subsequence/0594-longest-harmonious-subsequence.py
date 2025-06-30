class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        l = r = 0
        length = 0

        while r<len(nums):
            while nums[r]-nums[l]>1:
                l+=1
            if nums[r]-nums[l]==1:
                length = max(length,r-l+1)

            r+=1
        return length