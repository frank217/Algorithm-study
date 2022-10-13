#https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for i in range(n+1)]
        
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
            
        restrict_cnt = [0]*(n+1)
        restrict_cnt[n] = 1
        distance = [inf]*(n+1)
        distance[n] = 0
        discovered = [False] * (n+1)
        #       (distance, node)
        heap = [(0, n)]
        
        while heap:
            d, node = heapq.heappop(heap)
            if discovered[node] == True:
                continue
                
            discovered[node] = True
            distance[node] = d
            for nei, weight in g[node]:
                if not discovered[nei]:
                    heapq.heappush(heap, (d+weight, nei))
                elif distance[node] > distance[nei]:
                    restrict_cnt[node] += restrict_cnt[nei]
                    
        return restrict_cnt[1] % (10**9 + 7)
        