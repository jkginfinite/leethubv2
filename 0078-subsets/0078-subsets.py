from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combos = [[]]
        for i in nums:
            combos.append([i])
        for r in range(2,len(nums)+1):
            combos.extend(list(combinations(nums,r)))
        print(combos)
        return combos


        
        