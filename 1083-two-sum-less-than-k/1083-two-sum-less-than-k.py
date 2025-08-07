class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = -1
        left = 0
        right = len(nums)-1
        while left<right:
            Sum = nums[left]+nums[right]
            if Sum<k:
                answer = max(answer,Sum)
                left+=1
            else:
                right-=1
        return answer