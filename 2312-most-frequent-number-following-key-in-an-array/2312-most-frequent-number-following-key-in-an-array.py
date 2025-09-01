class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        from collections import Counter
        counts = Counter()
        for i in range(len(nums)-1):
            if nums[i]==key:
                counts[nums[i+1]]+=1
        res = max(counts,key=counts.get)
        return res   