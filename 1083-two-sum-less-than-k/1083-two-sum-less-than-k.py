class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_sum=-1
        for index1 in range(len(nums)):
            for index2 in range(index1+1,len(nums)):
                Sum = nums[index1]+nums[index2]
                if Sum<k:
                    max_sum = max(Sum,max_sum)

        return max_sum
        