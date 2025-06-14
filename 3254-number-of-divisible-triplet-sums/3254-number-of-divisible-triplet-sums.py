class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        if len(nums)<3:
            return 0
        res = 0
        for i in range(len(nums)-2):
            count = {}
            left = (d-nums[i])%d
            for j in range(i+1,len(nums)):
                if nums[j]%d in count:
                    res+=count[nums[j]%d]
                complement = (left-nums[j])%d
                if complement in count:
                    count[complement]+=1
                else:
                    count[complement]=1
        return res
            