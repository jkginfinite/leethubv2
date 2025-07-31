class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        count=0
        curr_sum=0
        prefix_sums = defaultdict(int)
        prefix_sums[0]=1 #base case

        for num in nums:
            curr_sum+=num
            count+=prefix_sums[curr_sum-k]
            prefix_sums[curr_sum]+=1
        return count