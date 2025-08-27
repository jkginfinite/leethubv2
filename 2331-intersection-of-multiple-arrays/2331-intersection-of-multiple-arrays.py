class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        N = len(nums)
        from collections import Counter

        arr =[]

        for num in nums:
            arr.extend(num)

        result = []
        count = Counter(arr)
        for element in count:
            if count[element]==N:
                result.append(element)
        return sorted(result)