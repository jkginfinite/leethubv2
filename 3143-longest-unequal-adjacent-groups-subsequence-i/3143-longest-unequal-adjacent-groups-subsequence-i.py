class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        #initialize over the words and their corresponding groups
        result = []
        #iterate over the words and their correspondiing groups
        #track the last group added to ans
        last = -1
        for i in range(len(words)):
            if groups[i]!=last:
                result.append(words[i])
                last = groups[i]
        return result