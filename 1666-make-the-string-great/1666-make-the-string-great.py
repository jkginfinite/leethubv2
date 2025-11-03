class Solution:
    def makeGood(self, s: str) -> str:

        def recursive(s):
            if not s:
                return ''
            string = s[0]
            for index in range(1,len(s)):
                if s[index].lower()==s[index-1].lower() and s[index]!=s[index-1]:
                    if index==1:
                        string = s[2:]
                        return recursive(string)
                    else:
                        return recursive(string[:index-1]+s[index+1:])
                string+=s[index]
            return string

        return recursive(s)