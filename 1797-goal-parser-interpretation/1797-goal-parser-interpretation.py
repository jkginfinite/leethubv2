class Solution:
    def interpret(self, command: str) -> str:
        C = list(command)
        r = ''
        i = 0
        n = len(command)
        while i<n:
            print(r)
            _ = C[i]
            if _=='G':
                r+=_
                i+=1
                pass
            else:
                if i+4<=n:
                    if ''.join(C[i:i+4])=='(al)':
                        r+='al'
                        i+=4
                        pass
                if i+2<=n:
                    if ''.join(C[i:i+2])=='()':
                            r+='o'
                            i+=2
                            pass
        return r