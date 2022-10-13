class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        # Use Dijkstra need to use heap
        # 1) get src 1 to destinaiton get scr1 to src2 to destination
        # 2) get 
        # 2) get cyclic graph
        # 3) get 
        
        graph = {}
        revGraph = {}
        for i in range(n):
            graph[i] = defaultdict(lambda:float("inf"))
            revGraph[i]= defaultdict(lambda:float("inf"))
        for u,v,w in edges:
            graph[u][v] = min(graph[u][v],w)
            revGraph[v][u] = min(revGraph[v][u],w)
        
        
        
        def dijkstra(src,g):
            mindist = defaultdict(lambda:float("inf"))
            mindist[src] = 0
            
            hq = [(0,src)]
            heapq.heapify(hq)
            

            while hq:
                dist, node = heapq.heappop(hq)
                #print(dist,node)
                for neigh,w in g[node].items():
                    newdist = w +dist
                    if newdist < mindist[neigh]:
                        mindist[neigh] = newdist
                        heapq.heappush(hq,(newdist,neigh))
            return mindist
        
        s1,s2,d1 = dijkstra(src1,graph), dijkstra(src2,graph),dijkstra(dest,revGraph)
        #print(s1)
        #print(s1[2],s2[2],d1[2])
        v = min([s1[i]+s2[i]+d1[i] for i in range(n)])
        v = min(v,s1[dest]+s2[dest])
        return -1 if v == float("inf") else v
            
                
        