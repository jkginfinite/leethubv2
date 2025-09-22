class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        tot = 0
        for i in nums:
            if len(str(i))>1:
                for j in str(i):
                    tot+=int(j)
            else:
                tot+=i
        return abs(tot-sum(nums))
        