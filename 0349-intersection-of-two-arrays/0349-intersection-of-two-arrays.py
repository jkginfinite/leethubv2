class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #return list(set(nums1).intersection(set(nums2)))
        #for i in nums2:
        #sort both arrays
        nums1.sort()
        nums2.sort()

        #initialize two pointers
        N = len(nums1)
        M = len(nums2)
        p1 = 0
        p2 = 0

        #create a set that stores integers appearing in both arrays
        intersection = set()
        while p1<N and p2<M:
            #add a value to the set of values if both pointers are equal
            if nums1[p1]==nums2[p2]:
                intersection.add(nums1[p1])
                p1+=1
                p2+=1
            elif nums1[p1]<nums2[p2]:
                p1+=1
            else:
                p2+=1
        
        #convert intersection to an array
        result = []
        for x in intersection:
            result.append(x)
        return result