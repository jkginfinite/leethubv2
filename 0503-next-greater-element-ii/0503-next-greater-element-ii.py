class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        return [next((x for x in nums[i+1:] + nums[:i] if x > nums[i]),-1) for i in range(len(nums))]

        #results = []
        #for i in range(len(nums)):
        #    _ = next((x for x in nums[i+1:]+nums[:i] if x>nums[i]),-1)
        #    results.append(_)
        #return results