class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        for i in range(count):
            for index in range(1,len(nums)):
                if nums[index-1]==0 and nums[index]!=0:
                    L = nums[index-1]
                    R = nums[index]
                    nums[index-1],nums[index] = R,L
            