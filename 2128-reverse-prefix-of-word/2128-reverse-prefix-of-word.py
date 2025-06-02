class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left = 0
        W = list(word)

        s = ''
        stopped = False
        while left!=len(word):
            L = W[left]
            s = L+s
            if L==ch:
                stopped = True
                break    
            else:
                left+=1
            
        
        if stopped:
            right = ''.join(W[left+1:])
            s+=right
            return s
        else:
            return word
        
        