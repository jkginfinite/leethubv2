class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxima = 0
        for s in sentences:
            maxima = max(maxima,len(s.split(' ')))
        return maxima
        