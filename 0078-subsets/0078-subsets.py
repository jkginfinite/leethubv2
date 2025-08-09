class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first,results,path):
            results.append(path[:])
            for i in range(first,N):
                path.append(nums[i])
                backtrack(i+1,results,path)
                path.pop()

        N = len(nums)
        results = []
        path = []
        first = 0
        backtrack(first,results,path)
        return results



            

        