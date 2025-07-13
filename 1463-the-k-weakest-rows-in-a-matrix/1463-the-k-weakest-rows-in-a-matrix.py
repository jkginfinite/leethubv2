class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = {}
        for index,row in enumerate(mat):
            d[index] = sum(row)
        d = sorted(d.items(),key=lambda x: x[1])
        return [v[0] for v in d][:k]