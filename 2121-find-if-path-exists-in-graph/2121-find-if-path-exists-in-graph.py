class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #strategy

        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False]*n
        seen[source] = True
        queue = collections.deque([source])

        #initialize an empty queue to store the nodes to be visited
        #user a bool array seen to mark all visited nodes and a hashmap graph to store all edges
        #add the starting node 0 to queue and mark it as visited
        #add the starting node 0 to queue and mark it as visited
        #if queue has nodes get the first node curr_node from queue. return true if curr_node is destination otherwise;
        #add all unvisited neighbor nodes of curr_node to queue and mark them as visited, then repeatstep 4
        #if we empties queue without funding destination, return false
        while queue:
            curr_node = queue.popleft()
            if curr_node == destination:
                return True
            
            for next_node in graph[curr_node]:
                if not seen[next_node]:
                    seen[next_node]=True
                    queue.append(next_node)
        return False