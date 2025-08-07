class Solution:
    def __init__(self):
        self.results = []
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        for index in range(len(nums)):
            val = nums[index]
            if val>0:
                break
            if index==0 or nums[index-1]!=nums[index]:
                self.twoSum(index,nums)
        return self.results

    def twoSum(self,i,nums):
        lo = i+1
        hi = len(nums)-1
        while lo<hi:
            val = nums[i]+nums[lo]+nums[hi]
            if val<0:
                lo+=1
            elif val>0:
                hi-=1
            else:
                _ = [nums[i],nums[lo],nums[hi]]
                self.results.append(_)
                lo+=1
                hi-=1
                while lo<hi and nums[lo]==nums[lo-1]:
                    lo+=1
        
            


        #twoSumII
        #set the low pointer to lo=i+1 and hi=len(arr)-1
        #while low pointer is smaller than high
        #if nums[i]+nums[lo]+nums[hi]<0 increment lo+=1
        # if nums[i]+nums[lo]+nums[hi]>0 then hi-=1
        # otherwise, add the three numbers to a result
        # decrement hi and increment lo
        