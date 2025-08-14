class Solution:
    def permute(self, n: int) -> List[List[int]]:
        results = []

        def bt(curr,index):
            if index==n:
                results.append(curr[:])
            
            else:
                for i in range(1,n+1):
                    if i not in curr and (not curr or curr[-1]%2!=i%2):
                        curr.append(i)
                        bt(curr,index+1)
                        curr.pop()

        bt([],0)
        return results
        