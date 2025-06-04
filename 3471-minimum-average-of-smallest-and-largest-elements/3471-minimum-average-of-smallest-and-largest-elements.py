class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        

        while nums:
            Maxx = max(nums)
            Minn = min(nums)
            avg = (Maxx+Minn)/2
            averages.append(avg)
            nums.remove(Maxx)
            nums.remove(Minn)
        return min(averages)