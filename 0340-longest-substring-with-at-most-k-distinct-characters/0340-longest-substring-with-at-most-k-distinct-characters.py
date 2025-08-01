class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        #use a hashmap counter to keep track of the number of eachh character in the current window
        #set max_size=0, iterate from 0 to n-1 at each step right, increment s[right]+=1 and increment 
        #counter[s[right]]+=1
        max_size = 0
        counter = collections.Counter() #use a hashmap counter to keep track of each character in the current window

        #set max_size=0 iterate right from 0 to n-1 at each step right, increment s[right] by 1 and increment counter[s[right]] by 1

        #if len(counter)>k decrement counter[s[right-max_size]] by -1 delete counter[s[right-max_size]] if it equals zero
        #otherwise increment max_size by 1

        for right in range(len(s)):
            counter[s[right]]+=1

            if len(counter)<=k:
                max_size+=1
            else:
                counter[s[right-max_size]]-=1

                if counter[s[right-max_size]]==0:
                    del counter[s[right-max_size]]

        return max_size