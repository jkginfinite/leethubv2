class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        def backtrack(index,results,path):
            results.append(path[:])
            for i in range(index,N):
                if i!=index and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1,results,path)
                path.pop()


        N = len(nums)
        index = 0
        results = []
        path = []
        backtrack(index,results,path)
        return results