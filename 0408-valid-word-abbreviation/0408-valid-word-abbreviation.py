class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i=j=0 #i for word, j for abbr
        while i<len(word) and j<len(abbr):
            if abbr[j].isdigit():
                if abbr[j]=='0':
                    return False #leading zero is invalid
                num=0
                while j<len(abbr) and abbr[j].isdigit():
                    num = num*10+int(abbr[j])
                    j+=1
                i+=num
            else:
                if i>=len(word) or word[i]!=abbr[j]:
                    return False
                i+=1
                j+=1
        return i==len(word) and j==len(abbr)

        #this is a two pointer approach where the pointers traverse the word and the abbreviation
        #if the rules are violated, return false. if they traverse to the end, then theyre correct