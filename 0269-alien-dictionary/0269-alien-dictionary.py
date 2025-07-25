class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        in_degree = Counter({c:0 for word in words for c in word})

        #step 1: we need to populate adjacency list and in_degree for each pair
        #of adjacent words
        for first_word, second_word in zip(words,words[1:]):
            for c,d in zip(first_word,second_word):
                if c!=d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d]+=1
                    break
            else: #check that second word isnt a prefix for first word
                if len(second_word)<len(first_word):
                    return ""
        
        #step 2: we need to repeatedly pick off nodes with an indegree of 0
        output = []
        queue = deque([c for c in in_degree if in_degree[c]==0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d]-=1
                if in_degree[d]==0:
                    queue.append(d)
        
        #if not all letters are in output, that means there was a cycle and so no valid ordering. Return "" as per the problem description
        if len(output)<len(in_degree):
            return ""
        #otherwise convert the ordering we found into a string and return it
        return "".join(output)