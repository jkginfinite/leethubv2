class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = 0
        Minn = min(nums)
        Maxx = max(nums)
        for i in nums:
            if i not in [Minn,Maxx]:
                count+=1
        return count



        