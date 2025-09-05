class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        queue = fruits
        taken = []
        while queue:
            f = queue.pop(0)
            index=0
            while index<len(baskets):
                b = baskets[index]
                print(f"f:{f}, b:{b}")
                if f<=b and index not in taken:
                    #taken.append(index)
                    baskets.pop(index)
                    index=len(baskets)
                else:
                    index+=1
                print(taken)
                print('\n')
        return len(baskets)-len(taken)
        