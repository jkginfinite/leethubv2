class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n, ans = len(nums), inf

        nums.sort()

        for left, right in zip(nums[:n//2], nums[n-1: n//2-1: -1]):
            print(left)
            print(right)
            ans = min(ans, left+right)

        return ans/2