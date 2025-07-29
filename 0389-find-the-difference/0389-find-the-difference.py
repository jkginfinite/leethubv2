class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        
        sC = Counter(s)
        tC = Counter(t)

        for key in tC.keys():
            if key not in sC.keys() or tC[key]!=sC[key]:
                return key
        