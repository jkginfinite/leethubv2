class Solution:
    def arrangeCoins(self, n: int) -> int:
        import numpy as np
        val = (2*n+1/4)**(1/2)-(1/2)
        return int(np.floor(val))
        