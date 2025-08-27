class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    
        ans1 = []
        for n1 in nums1:
            if n1 not in nums2 and n1 not in ans1:
                ans1.append(n1)

        ans2 = []
        for n2 in nums2:
            if n2 not in nums1 and n2 not in ans2:
                ans2.append(n2)
        
        return [ans1,ans2]