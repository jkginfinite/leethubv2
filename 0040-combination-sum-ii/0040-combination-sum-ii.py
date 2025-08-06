class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def backtrack(start,path,total):
            if total==target:
                results.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue #skip duplicates
                if total+candidates[i]>target:
                    break #early stopping
                path.append(candidates[i])
                backtrack(i+1,path,total+candidates[i])
                path.pop()
        backtrack(0,[],0)
        return results