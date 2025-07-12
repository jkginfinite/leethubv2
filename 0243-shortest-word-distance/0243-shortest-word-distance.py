class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        indices1 = []
        indices2 = []
        if wordsDict.count(word1)==1:
            index1 = wordsDict.index(word1)
        else:
            for index, word in enumerate(wordsDict):
                if word==word1:
                    indices1.append(index)
        if wordsDict.count(word2)==1:
            index2 = wordsDict.index(word2)
        else:
            for index, word in enumerate(wordsDict):
                if word==word2:
                    indices2.append(index)

        min_diff = 1e50
        if indices1 and indices2:
            for i1 in indices1:
                for i2 in indices2:
                    min_diff = min(abs(i1-i2),min_diff)
        elif indices1 and not indices2:
            for i1 in indices1:
                min_diff = min(abs(i1-index2),min_diff)

        elif not indices1 and indices2:
            for i2 in indices2:
                min_diff = min(abs(index1-i2),min_diff)
        else:
            min_diff = abs(index1-index2)
        return min_diff
