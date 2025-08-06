class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #back tracking - general algorithm for finding all or some solutions to some computational problems
        #the idea is that it incrementally builds candidates to the solutions, and abandons a candidate (backtrack)
        #as soo as it determines that this candidate cannot lead to a final solution
        #we incrementally build a combination, and once we find it its not valid we backtrack by discarding
        """
        []
        [3] - [3,3], [3,4], [3,5] now from these [3,3]<target and [3,4]<target so try -> [3,3,3], [3,4,4] but discar because sum>target
        keep 3,5

        [4] <target, try [4,4] sum=target, try [4,5] discard

        [5]<target, try [5,5]>target
        """

        results = []
        def backtrack(remain, comb, start):
            if remain==0:
                results.append(list(comb))
                return
            elif remain<0:
                return
            
            for i in range(start, len(candidates)):
                #add the number into the combination
                comb.append(candidates[i])
                #give the current number another chance, rather than moving on
                backtrack(remain-candidates[i],comb,i)
                #backtrack, remove the number from the combination
                comb.pop()
        backtrack(target,[],0)

        return results
        