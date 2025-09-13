class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        median = m * n // 2 + 1
        
        def helper(val: int) -> int:
            cnt = 0
            for row in grid:
                l, r = 0, n - 1
                while l <= r:
                    mid = (l + r)//2
                    if row[mid] > val:
                        r = mid - 1
                    else:
                        l = mid + 1
                cnt += l
            return cnt >= median

        l, r = 1, 10 ** 6
        while l <= r:
            mid = (l + r)//2
            if helper(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l