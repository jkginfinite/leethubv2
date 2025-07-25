class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        rules = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'DM':900}
        d.update(rules)
        values = d
        total=0
        i=0
        while i<len(s):
            #if this is the subtractive case
            if i+1<len(s) and values[s[i]]<values[s[i+1]]:
                total += values[s[i+1]] - values[s[i]]
                i+=2
            else:
                total+=values[s[i]]
                i+=1
        return total


        