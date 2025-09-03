class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:


        def lowerBound(nums,target):
            low = 0
            high = len(nums)-1
            index = len(nums)
            while low<=high:
                mid = (low+high)//2

                if nums[mid]>=target:
                    high = mid-1
                    index = mid
                else:
                    low = mid+1

            return index

        firstIndex = lowerBound(nums,target)
        return firstIndex + len(nums)//2 <len(nums) and nums[firstIndex+len(nums)//2]==target      