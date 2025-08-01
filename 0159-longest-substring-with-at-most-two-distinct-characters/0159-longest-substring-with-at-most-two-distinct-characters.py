class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        if len(s)<=2:
            return len(s)
        queue = []
        queue_set = set()
        max_len = 0
        for i in s:
            queue.append(i)
            if len(set(queue))<=2:
                max_len = max(max_len,len(queue))
            elif len(set(queue))>2:
                while len(set(queue))>2:
                    queue.pop(0)
        return max_len


        #eceba
        
        #e q = [e] qs = {ec}
        #ec save q=[ec] qs = {ec}
        #ece# save q=[ece] qs = {ec}
        #eceb pop first 
        #ceb pop first
        #e
        #ceba pop first
        #

        #ccaabbb

        #c
        #cc
        #cca save
        #ccaa save
        #ccaab pop first, 
        #caab pop first again 
        #aab save
        #aabb save result
        #aabbb save reuslt 
        