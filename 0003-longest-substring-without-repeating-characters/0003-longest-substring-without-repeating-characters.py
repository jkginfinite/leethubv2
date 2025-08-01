class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = []
        max_len = 0
        for i in s:
            if i not in queue:
                queue.append(i)
                max_len = max(max_len,len(queue))
            else:
                while i in queue:
                    queue.pop(0)
                if queue:
                    queue.append(i)
                else:
                    queue = [i]
        return max_len
        