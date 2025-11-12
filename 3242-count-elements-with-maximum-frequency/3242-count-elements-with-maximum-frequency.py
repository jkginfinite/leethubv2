class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import Counter


        count = Counter(nums)
        maxx = max(count.values())
        c = 0
        for i in nums:
            if count[i]==maxx:
                c+=1
        return c