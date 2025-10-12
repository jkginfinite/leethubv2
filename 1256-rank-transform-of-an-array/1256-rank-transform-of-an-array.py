class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = set(arr)
        L = sorted(list(s))
        print(L)
        d = {}
        n=1
        for j in L:
            d[n]=j
            n+=1
        dd = dict(zip(d.values(),d.keys()))
        L = []
        for a in arr:
            L.append(dd[a])
        return L