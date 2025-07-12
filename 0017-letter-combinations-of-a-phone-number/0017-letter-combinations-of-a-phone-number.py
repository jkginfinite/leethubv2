from itertools import combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],
        7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        
        letters = []
        for s in digits:
            elements = d[int(s)]
            if not letters:
                letters.extend(elements)
            else:
                _ = []
                for i in letters:
                    for j in elements:
                        _.append(i+j)
                        #elif i>j:
                        #    _.append(j+i)
                        #else:
                        #    _.append(i+j)
                letters = _
        return letters

        #return set(letters_all).difference(letters_individual)

        