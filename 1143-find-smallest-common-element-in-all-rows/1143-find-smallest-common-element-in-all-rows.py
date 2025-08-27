class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        N = len(mat)

        from collections import Counter

        arr = []
        for elem in mat:
            arr.extend(elem)

        count = Counter(arr)
        result = []
        for elem in count:
            if count[elem]==N:
                result.append(elem)
        if result:
            return min(result)
        return -1