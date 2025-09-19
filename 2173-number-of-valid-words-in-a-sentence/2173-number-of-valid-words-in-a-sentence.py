class Solution:
    def countValidWords(self, sentence: str) -> int:
        count = 0
        for w in sentence.split():
            ok = True
            hypens, punctu = 0,0
            for i,c in enumerate(w):
                if c.isdigit():
                    ok = False
                    break
                if c=='-':
                    hypens+=1
                    if hypens>1 or i==0 or i==len(w)-1 or not w[i-1].isalpha() or not w[i+1].isalpha():
                        ok = False
                        break
                if c in '!.,':
                    punctu+=1
                    if punctu>1 or i!=len(w)-1:
                        ok = False
                        break
            if ok:
                count+=1
        return count