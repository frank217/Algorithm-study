class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        
        for u,v in roads:
            graph[u].add(v)
            graph[v].add(u)
        
        maxrank = 0
        
        for i in range(n):
            l = len(graph[i])

            for j in range(i+1,n):
                v = l + len(graph[j])
                if j in graph[i]:
                    v -= 1
                maxrank = max(maxrank,v)
        
        return maxrank
            