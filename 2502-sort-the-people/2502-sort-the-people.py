class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        #
        heights = [str(i) for i in heights]
        d = dict(zip(heights,names))

        return [j[1] for j in sorted(d.items(),key = lambda x: int(x[0]),reverse=True)]

