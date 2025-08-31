class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter

        Count = Counter(words)
        Count = {key:value for key,value in Count.items()}
        Count = dict(sorted(Count.items(), key=lambda item: item[1],reverse=True))

        L = []
        #print(Count)
        max_count = max(Count.values())
        for value in range(max_count,0,-1):
            _ = set([key for key in Count.keys() if Count[key]==value])
            _ = sorted(_)
            L.extend(_)
        return L[:k]

