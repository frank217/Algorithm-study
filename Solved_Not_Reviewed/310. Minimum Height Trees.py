class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # solution 1 Run BFS on every thing O(E(E + V)) = 8 * 10^8
        # TLE
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        res = []
        minHeight = float("inf")
        for rootnode in range(n) :
            dq = deque([(rootnode,0)])
            visited = set()
            maxDist = 0
            while dq:
                node,dist = dq.popleft()
                maxDist = max(maxDist,dist)
                for cn in graph[node]:
                    if cn not in visited:
                        visited.add(node)
                        dq.append((cn,dist+1))
            #print(rootnode,maxDist,minHeight,res)

            if maxDist < minHeight:
                minHeight = maxDist
                res = [rootnode]
            elif maxDist == minHeight:
                res.append(rootnode)
        return res
                        
        # Solution 2 Leaf removal.
        # The result only return the center of MHT. 
        # Since this is acyclic graph, leave node will only have one edge.
        # remove the edges until there are only 1 or 2 node left.
        # There can only be 1 or 2 node because 
        # 1 node then at least 2 subtree have same max MHT
        # if the max MHT are only 1 subtree then 
        #   a) one subtree 
        # 2 node then there are least two MHT with height diff only 1. 
        # 3 node then 
        if n <= 2:
            return list(range(n))
        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        leaves = [node for node in graph if len(graph[node]) == 1]
        remain = n
        while remain > 2:
            newleaves = []
            remain -= len(leaves)
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1 :
                        newleaves.append(neighbor)
            leaves = newleaves
        
        return list(leaves)
