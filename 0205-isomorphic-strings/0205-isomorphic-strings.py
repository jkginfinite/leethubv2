class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s==t:
            return True
        
        if len(s)!=len(t):
            return False

        S = list(s)
        T = list(t)
        d = {}
        for index in range(len(S)):
            s_element = S[index]
            t_element = T[index]
            if s_element not in d and t_element not in list(d.values()):
                d[s_element] = t_element
            elif (s_element in d and d[s_element]!=t_element) or (t_element in list(d.values()) and s_element not in d):
                return False
        return True
