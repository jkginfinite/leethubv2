class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i=j=0
        while j<len(abbr) and i<len(word):
            if abbr[j].isalpha():
                if abbr[j]!=word[i]:
                    return False
                i+=1
                j+=1
            else:
                if abbr[j]=='0':
                    return False
                temp=0
                while j<len(abbr) and abbr[j].isdigit():
                    temp = temp*10+int(abbr[j])
                    j+=1
                i+=temp

        return j==len(abbr) and i==len(word)