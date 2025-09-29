class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        mark = [False]*len(S)
        
        for word in words: 
            k = -1
            while True: 
                k = S.find(word, k+1)
                if k == -1: break 
                mark[k:k+len(word)] = [True]*len(word)
        
        ans = []
        for i in range(len(S)): 
            if mark[i] and (i == 0 or not mark[i-1]): 
                ans.append("<b>")
            ans.append(S[i])
            if mark[i] and (i+1 == len(S) or not mark[i+1]): 
                ans.append("</b>")
        return "".join(ans)