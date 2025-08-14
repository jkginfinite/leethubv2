class Solution:
    def permute(self, N: int, K: int) -> List[int]:
        ans = []
        vals = list(range(1,N+1))
        want = 1

        for t in range(N):
            ways = factorial(N-1-t>>1)*factorial(N-t>>1)

            for i,v in enumerate(vals):
                if v%2!=want and (t or N%2):
                    continue
                if K<=ways:
                    break
                K-= ways
            else:
                return []

            ans.append(vals.pop(i))
            want = ans[-1]&1^1

        return ans