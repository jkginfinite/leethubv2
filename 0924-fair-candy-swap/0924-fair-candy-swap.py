class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sA = sum(aliceSizes)
        sB = sum(bobSizes)

        setB = set(bobSizes)
        for x in aliceSizes:
            if x+(sB-sA)/2 in setB:
                return [x,x+(sB-sA)/2]