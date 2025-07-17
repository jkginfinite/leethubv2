class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp=[[0]*k for _ in range(k)]
        res = 0
        for cur in nums:
            cur%=k
            for prev in range(k):
                dp[prev][cur] = dp[cur][prev]+1
                res = max(res, dp[prev][cur])
        return res