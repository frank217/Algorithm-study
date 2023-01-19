# Hard
#https://leetcode.com/contest/weekly-contest-328/problems/difference-between-maximum-and-minimum-price-sum/

class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        # Dijkstra with getting maxium path val.??
        # Start with Leaf node( only one path) in heap
        
        graph = defaultdict(list)
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        @cache
        def dfs(node,parent):
            m = 0
            for n in graph[node]:
                if n != parent:
                    m = max(m,dfs(n,node))
            return price[node] + m
        
        ans = 0
        for node in range(n):
            maxV = dfs(node,-1)
            minV = price[node]
            ans = max(maxV-minV,ans)
        return ans
                    