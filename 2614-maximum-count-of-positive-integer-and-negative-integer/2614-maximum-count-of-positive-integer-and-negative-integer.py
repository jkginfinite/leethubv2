class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0

        for i in nums:
            if i!=0:
                if i>0:
                    pos+=1
                else:
                    neg+=1

        return max(pos,neg)
        