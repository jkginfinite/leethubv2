class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        #create a variable n and initialize it to the size of nums
        #create a list of missing ranges that will contain the solution to the problem
        #if there are no element in nums, we simply return the range [lower, upper]
        #we check if the first element in the array is equal. lower or not, if lower<nums[0], we have a missing range [lower, nums[0]-1] we add it to missingRanges
        #we iterate over all the elements in nums using a loop that runs from i=0 to n-2 till the second last element
        #if the current element nums[i] and next element nums[i+1] differ by 1 or loss, there are no missing numbers from nums[i]+1 to nums[i+1]-1. As a result [nums[i]+1, nums[i+1]-1] is added to missingRanges

        #we check if the last element of the array is equal to upper or not. if nums[i-1]<upper we have a missing range [nums[n-1]+1, upper]. we again add it to missingRanges
        n = len(nums)
        missing_ranges = []
        if n==0:
            missing_ranges.append([lower,upper])
            return missing_ranges
        
        #check for any missing numbers between the lower bound and nums[0]
        if lower<nums[0]:
            missing_ranges.append([lower,nums[0]-1])
        
        #check for any missing numbers between successive elements of nums
        for i in range(n-1):
            if nums[i+1]-nums[i]<=1:
                continue
            missing_ranges.append([nums[i]+1,nums[i+1]-1])

        #check for any missing numbers between the last element of nums and the upper bound
        if upper>nums[n-1]:
            missing_ranges.append([nums[n-1]+1,upper])
        
        return missing_ranges