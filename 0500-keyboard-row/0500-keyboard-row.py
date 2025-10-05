class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"

        ret = []
        for W in words:
            w = W.lower()
            if all([j in first_row for j in w]) or all([jj in second_row for jj in w]) or all([jjj in third_row for jjj in w]):
                ret.append(W)
        return ret