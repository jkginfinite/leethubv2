class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = list(pattern)
        S = s.split(' ')
        if len(p)!=len(S):
            return False
        d = {}

        for index in range(len(S)):
            p_element = p[index]
            s_element = S[index]
            if p_element not in d and s_element not in list(d.values()):
                d[p_element] = s_element
            elif p_element in d and d[p_element]!=s_element:
                return False
            elif s_element in list(d.values()) and p_element not in d:
                return False
        return True
        