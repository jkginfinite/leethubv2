class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        from collections import Counter

        arr = arr1+arr2+arr3

        count = Counter(arr)

        intersect = []
        for element in count:
            if count[element]==3:
                intersect.append(element)

        return intersect