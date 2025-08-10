class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        possible_numbers = list(range(1,10))
        if k==0:
            return [0]
        if k==1:
            return [n]
        if n>sum(possible_numbers):
            return []

        results = []
        def backtrack(remain,combination,start):
            if remain==0 and len(combination)==k:
                results.append(combination[:])
                return 

            elif remain<0:
                return
            
            for i in range(start,len(possible_numbers)):
                if possible_numbers[i] in combination:
                    continue
                combination.append(possible_numbers[i])
                backtrack(remain-possible_numbers[i],combination,i)
                combination.pop()
        
        remain = n
        combination = []
        start = 0
        backtrack(remain,combination,start)
        return results