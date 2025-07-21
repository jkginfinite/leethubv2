class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #make a copy of the first m elements of nums1
        nums1_copy = nums1[:m]

        #read pointers for nums1copy and nums2 respectively
        p1=0
        p2=0

        #compare elements from num1copy and nums2 and write smallest to nums1
        for p in range(n+m):
            if p2>=n or (p1<m and nums1_copy[p1]<=nums2[p2]):
                nums1[p]=nums1_copy[p1]
                p1+=1
            else:
                nums1[p]=nums2[p2]
                p2+=1