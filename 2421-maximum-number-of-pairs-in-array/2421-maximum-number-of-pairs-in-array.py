class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        from collections import Counter

        new_dict = Counter(nums)
        pairs = 0
        left_over = 0
        for key in new_dict:
            if new_dict[key]==1:
                left_over+=1
            elif new_dict[key]%2==0:
                pairs += new_dict[key]//2
            else:
                left_over+=1
                pairs += (new_dict[key]-1)//2
                
        return [pairs, left_over]
        