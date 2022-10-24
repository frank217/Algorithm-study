#https://leetcode.com/problems/build-a-matrix-with-conditions/


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Need to sort? ask it if it is possible to insert?
        # Topological sort? 
        # If Circular than can't work. most to least. 
        # Count incoming edge
        
        def topologicalSort(conditions):
            graph = defaultdict(list)
            indegree = defaultdict(int)

            for a,b in conditions:
                graph[a].append(b)
                indegree[b] += 1

            # When will it not work?
            # Circular will not work
            # Others will work.
            root = set(range(1,k+1))
            root.difference_update(set(indegree.keys()))
            #print(root)

            # Topological sort
            q = deque(root)
            rowOrder= []
            while q:
                node = q.popleft()
                rowOrder.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0 :
                        q.append(neighbor)

            # After topological sort if there is any none processed node there is cyclic graph. return empty matrix.
            if len(rowOrder) < k: return[]
            return rowOrder
        
        r = topologicalSort(rowConditions)
        c = topologicalSort(colConditions)
        #need to get 
        print("row :", r)
        print("col :", c)

        index = {}
        if r and c:
            
            for i in range(k):
                if r[i] in index:
                    index[r[i]][0] = i
                else:
                    index[r[i]] = [i,0]
                if c[i] in index:
                    index[c[i]][1] = i
                else:
                    index[c[i]] = [0,i]
        else:
            return []
        
        #print(index)
        ans = [[0 for i in range(k)] for j in range(k)]
        for key, value in index.items():
            ans[value[0]][value[1]] = key
        #print("ans",ans)
        return ans
                
                

    
        
        
        