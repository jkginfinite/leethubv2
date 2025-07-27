class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for index in range(1,len(nums)):
            curr = nums[index]
            last = nums[index-1]
            if (curr%2==0 and last%2==0) or (curr%2!=0 and last%2!=0):
                return False
        return True
        