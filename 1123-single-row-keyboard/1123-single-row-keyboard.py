class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        last = 0
        L = list(keyboard)
        moves = 0
        for letter in word:
            moves += abs(L.index(letter) - last)
            last = L.index(letter)
        return moves