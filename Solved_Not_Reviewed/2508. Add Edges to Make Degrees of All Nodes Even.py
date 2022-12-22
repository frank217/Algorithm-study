# weekly-contest-324
#   https://leetcode.com/contest/weekly-contest-324/problems/add-edges-to-make-degrees-of-all-nodes-even/


class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        graph = defaultdict(set)
        
        for a,b in edges:
            indegree[a] +=1
            indegree[b] +=1
            graph[a].add(b)
            graph[b].add(a)
            
        oddedgeNode = []
        for node,degree in indegree.items():
            if degree % 2 :
                # If odd and n edges, can't add.
                if degree == n-1:
                    return False
                oddedgeNode.append(node)
        
        ll = len(oddedgeNode)
        #print(oddedgeNode)
        #for node in oddedgeNode:
        #    print(node,indegree[node],graph[node])
        #print(graph)
        if ll <= 4 and ll % 2 == 0:
            
            if ll == 0 :
                return True
            elif ll == 2:
                a,b = oddedgeNode
                if a not in graph[b]:
                    return True
                for i in range(1,n+1):
                    if a not in graph[i] and b not in graph[i]:
                        return True
            else:
                a,b,c,d = oddedgeNode
                if (a not in graph[b] and c not in graph[d]) or (a not in graph[c] and b not in graph[d]) or (a not in graph[d] and c not in graph[b]):
                    return True
        return False
        