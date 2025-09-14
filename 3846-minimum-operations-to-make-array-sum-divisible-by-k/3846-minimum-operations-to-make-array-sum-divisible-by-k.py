class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if sum(nums)%k==0:
            return 0
        
        S = sum(nums)
        count = 0
        while S%k!=0:
            S-=1
            count+=1
        return count
        