class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        from collections import Counter
        c = Counter(s)
        v = ''
        for u in s:
            if c[u]<k:
                v+=u
        return v
        