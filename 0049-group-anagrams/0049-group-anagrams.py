class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Steps:
        loop through each string, sorting the characters and converting the sorted list to a string, saving that string to a new list
save these sorted strings to a set to remove duplicates
create a dictionary where the keys are the set of sorted strings and the values are empty lists
loop through the set in step 1, adding all the indices where they key matched
create an empty list
loop through the dictionary in step 4, using the indices to identify the words and appending them to a list
Return the list of step5
        """
        sorts = []
        sortsSet = set()
        for s in strs:
            S = ''.join(sorted(s)) #step 1
            sorts.append(S) #step 1
            sortsSet.add(S) #step 2
        
        
        d = {key:[] for key in sortsSet} #step3
        for index in range(len(sorts)):
            key = sorts[index]
            d[key].append(index) #step 4
        
        elements = [] #step 5
        for key in d.keys():
            u = []
            for value in d[key]:
                u.append(strs[value])
            elements.append(u)  #step 6
        return elements #step 7
                