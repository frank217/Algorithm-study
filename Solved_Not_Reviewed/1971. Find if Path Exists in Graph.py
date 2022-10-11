#https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Use BFS 
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        dq = deque([source])
        visited = set()
        while dq:
            node = dq.popleft()
            visited.add(node)
            
            if node == destination:
                return True
            for connectedNode in graph[node]:
                if connectedNode not in visited:
                    dq.append(connectedNode)
        return False 
            
        
        