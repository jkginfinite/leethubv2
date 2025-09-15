class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def isNice(string):
            for letter in string:
                if not (letter.upper() in string and letter.lower() in string):
                    return False
            return True

        max_len = 0
        d = {}
        for sublength1 in range(len(s)):
            for sublength2 in range(sublength1,len(s)+1):
                substring = s[sublength1:sublength2]
                print(substring)
                if isNice(substring):
                    max_len = max(max_len,len(substring))
                    if len(substring) not in d:
                        d[len(substring)] = []
                    d[len(substring)].append(substring)

        return d[max_len][0]

        