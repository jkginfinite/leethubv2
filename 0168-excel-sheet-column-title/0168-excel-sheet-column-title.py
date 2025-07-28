class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber>0:
            columnNumber-=1
            #get the last character and append it at the end of the string
            ans+=chr(columnNumber%26+ord("A"))
            columnNumber//=26
        
        #reverse it, as we appended characters in reverse order
        return ans[::-1]