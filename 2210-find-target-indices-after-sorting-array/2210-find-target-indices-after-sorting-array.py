class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        def lower_bounds(nums,target):
            left,right = 0, len(nums)
            while left<right:
                mid = (left+right)//2
                if nums[mid]<target: #subtle difference <
                    left = mid+1
                else:
                    right = mid
            return left
        
        def upper_bounds(nums, target):
            left, right=0, len(nums)
            while left<right:
                mid = (left+right)//2
                if nums[mid]<=target: #subtle difference <=
                    left = mid+1
                else:
                    right = mid
            return left
        
        low = lower_bounds(nums,target)
        high = upper_bounds(nums,target)

        if low==high:
            return []
        return list(range(low,high))
        
        