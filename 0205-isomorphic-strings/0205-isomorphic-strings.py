class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #strategy
        #loop through the string s, count the number of times the characters appear save that count to a list
        #loop throughg the string t, count the number of times the characters appear save to list
        #sort each list
        if s==t:
            return True

        from collections import Counter
        cs = Counter(s)
        ct = Counter(t)
        count = sorted(cs.values())==sorted(ct.values())

        if not count or len(s)!=len(t):
            return False

        S = list(s)
        T = list(t)
        d = {}
        for index in range(len(S)):
            s_element = S[index]
            t_element = T[index]
            if s_element not in d and t_element not in list(d.values()):
                d[s_element] = t_element
            elif s_element in d and d[s_element]!=t_element:
                return False
            elif t_element in list(d.values()) and s_element not in d:
                return False
        return True
        
        return count