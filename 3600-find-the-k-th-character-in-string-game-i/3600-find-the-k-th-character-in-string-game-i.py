class Solution:
    def kthCharacter(self, k: int) -> str:
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        i=0
        word = 'a'
        while len(word)<k:
            new = ''
            for i in word:
                index = alphabet.index(i)
                if index+1<26:
                    next_char = alphabet[index+1]
                else:
                    next_char = alphabet[(26%index)+1]
                new+=next_char
            word+=new
        return word[k-1]