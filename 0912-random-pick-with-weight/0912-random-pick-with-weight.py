import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.weights = [w[i]/sum(w) for i in range(len(w))]

    def pickIndex(self) -> int:
        index = random.choices(range(len(self.w)),weights=self.weights,k=1)[0]
        print(index)
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()