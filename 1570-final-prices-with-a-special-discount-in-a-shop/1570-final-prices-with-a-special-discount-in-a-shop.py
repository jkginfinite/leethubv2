class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        results = []
        for index in range(len(prices)):
            p = prices[index]
            subtract = 0
            if index+1<len(prices):
                queue = prices[index+1:]
                while queue:
                    node = queue.pop(0)
                    if node<=p:
                        subtract+=node
                        break
            results.append(p-subtract)
        return results
        