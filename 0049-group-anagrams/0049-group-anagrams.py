class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #loop through the list
        #sort each string, saving the index of each
        #for the sorted list, identify indicies that are equal when sorted
        #loop through these indices, append the result to a list
        sorts = []
        sortsSet = set()
        for s in strs:
            S = ''.join(sorted(s))
            sorts.append(S)
            sortsSet.add(S)
        
        L =[]
        for e in sortsSet:
            L.append(e)
        
        d = {key:[] for key in L}
        for index in range(len(sorts)):
            key = sorts[index]
            d[key].append(index)
        
        elements = []
        for key in d.keys():
            u = []
            for value in d[key]:
                u.append(strs[value])
            elements.append(u)
        return elements
                