class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        Maxx = 0
        D = {}

        for index in range(1,len(nums)):
            curr = nums[index]
            prev = nums[index-1]
            if prev == key:
                if curr not in D:
                    D[curr]=0
                D[curr]+=1
                Maxx = max(Maxx,D[curr])
        return [key for key in D.keys() if D[key]==Maxx][0]   