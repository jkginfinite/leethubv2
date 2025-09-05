class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        queue = fruits
        while queue:
            f = queue.pop(0)
            index=0
            while index<len(baskets):
                b = baskets[index]
                if f<=b:
                    baskets.pop(index)
                    index=len(baskets)
                else:
                    index+=1
        return len(baskets)
        