class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def binarySearch(arr,i):
            low=0
            high=len(arr)-1
            while low<=high:
                mid = low+(high-low)//2
                if arr[mid]==i:
                    return mid
                elif arr[mid]<i:
                    low = mid+1
                else:
                    high = mid-1
            return -1

        Minn = float('inf')
        for i in nums1:
            _ = binarySearch(nums2,i)
            if _!=-1:
                Minn = min(Minn,i)
        if Minn!=float('inf'):
            return Minn
        return -1