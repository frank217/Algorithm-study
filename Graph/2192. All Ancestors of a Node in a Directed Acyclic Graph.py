#https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/


# Graph Problem, Topological sort

from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        # Solution 1 bruforce. check all the Ancestor each time
        # Possible runtime O(N^2)
        dic = defaultdict(list)
        rootNodes = set([i for i in range(n)])
        for f,t in edges:
            dic[t].append(f)
            if t in rootNodes:
                rootNodes.remove(t)
        res = []
        for i in range(n):
            parentNode = list(dic[i])
            ancestor = set()
            #print(i,dic)
            while parentNode:
                node = parentNode.pop()
                if node not in ancestor:
                    ancestor.add(node)
                    parentNode += dic[node]
                    #print(i,node,parentNode)
            res.append(sorted(ancestor))
        return res
            
        # Solution 2 : Topological Sort
        # runtime O(N*M) where N - # of node, M - # of edge
        #
        # Algorithm is very similar to BFS where it will add node by each level starting from Root node. 
        # However this algorithm only adds the node if all the edge direct to the node are consumed.
        # where as BFS will add the node when first seen. 
        # As a result this algorithm will only add node when all its parent nodes have been consume by algorithm.
        # which is perfect for checking all the ancestor since the node will only be added once its parent node has 
        # found all their ancestor. 

        edge = defaultdict(list)
        ingestion = defaultdict(int)
        for f,t in edges:
            edge[f].append(t)
            ingestion[t] += 1 
            
        dq = deque([i for i in range(n) if ingestion[i] == 0])
        res = [set() for i in range(n)]

        while dq:
            fromNode = dq.popleft()
            
            for toNode in edge[fromNode]:
                res[toNode].add(fromNode)
                res[toNode] |= res[fromNode]
                
                ingestion[toNode] -= 1
                if ingestion[toNode] == 0:
                    dq.append(toNode)
        
        return list(map(sorted,res))
        
        
        
                
                
            