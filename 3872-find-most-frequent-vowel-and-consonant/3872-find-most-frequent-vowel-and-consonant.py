class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a':0,'e':0,'i':0,'o':0,'u':0}
        letters = list('abcdefghijiklmnopqrstuvwxyz')
        c = [a for a in letters if a not in vowels.keys()]
        consonants = {key:0 for key in c}
        for k in s:
            if k in vowels.keys():
                vowels[k]+=1
            else:
                consonants[k]+=1

        return max(vowels.values())+max(consonants.values())
        