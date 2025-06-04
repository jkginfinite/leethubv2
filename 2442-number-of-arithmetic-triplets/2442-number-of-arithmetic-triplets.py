class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count=0
        L = len(nums)
        for i in range(L):
            for j in range(i+1,L):
                for k in range(j+1,L):
                    if (nums[j]-nums[i])==diff and (nums[k]-nums[j])==diff:
                        count+=1
        return count