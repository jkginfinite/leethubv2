class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        words = [w for w in words if len(w)==len(pattern)]
        P = list(pattern)
        r = []
        for w in words:
            d = {}
            S = list(w)
            p = False
            for index in range(len(w)):
                p_element = P[index]
                s_element = S[index]
                if p_element not in d and s_element not in list(d.values()):
                    d[p_element] = s_element
                elif (p_element in d and d[p_element]!=s_element) or (s_element in list(d.values()) and p_element not in d):
                    p = True
            if not p:
                r.append(w)
        return r