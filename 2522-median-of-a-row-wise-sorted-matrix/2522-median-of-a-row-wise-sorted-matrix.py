class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        L = []

        for row in grid:
            for cell in row:
                L.append(cell)

        L.sort()

        import numpy as np
        return int(np.median(L))