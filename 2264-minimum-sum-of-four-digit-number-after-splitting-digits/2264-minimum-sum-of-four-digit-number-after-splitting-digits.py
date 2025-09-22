class Solution:
    def minimumSum(self, num: int) -> int:
        numz = str(num)
        from itertools import permutations

        indices = ['0','1','2','3']
        L = []
        for i in range(2,4):
            _ = list(permutations(indices,i))
            for j in _:
                indices1 = ''.join(j)
                u = [v for v in indices if v not in j]
                indices2 = ''.join(u)
                L.append([indices1,indices2])
                L.append([indices1[::-1],indices2])
                L.append([indices1,indices2[::-1]])
                L.append([indices1[::-1],indices[::-1]])
        print(L)
        minn = float('inf')
        for combo in L:
            nums1_indices,nums2_indices = combo
            nums1 = ''
            nums2 = ''
            for n1 in nums1_indices:
                nums1+= numz[int(n1)]
            for n2 in nums2_indices:
                nums2+= numz[int(n2)]
            #nnn = int(nums1)+int(nums2)
            #print(f"{nums1}+{nums2} = {nnn}")
            
            minn = min(int(nums1)+int(nums2),minn)
        return minn