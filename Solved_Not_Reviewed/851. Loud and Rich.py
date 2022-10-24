#https://leetcode.com/problems/loud-and-rich/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # Find least quiet person that is topologically strictly higher or same, meaning getting
        # most quiet person among its topological ancestor
        
        # There is no circular loop(Given, so no need to check for circular loop)
        # Looks like quiet is unique(otherwise require ordering if quietness is same)
        
        # Get the ordering 
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for a,b in richer:
            graph[a].append(b)
            indegree[b] += 1 
        
        root = set([i for i in range(len(quiet))]).difference(set(indegree.keys()))
        
        #tuple of current node and most quiet person including oneself and ancestor.
        # Since root node only have one self it is the quitest node. 
        dq = deque([(node,node) for node in root])
        track = {}
        while dq:
            node,mostQuietNode = dq.popleft()
            track[node] = mostQuietNode
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if neighbor not in track:
                    track[neighbor] = mostQuietNode
                elif quiet[mostQuietNode] < quiet[track[neighbor]] :
                    track[neighbor] = mostQuietNode
                
                mostQuietNodeSoFar =  track[neighbor] if quiet[track[neighbor]] < quiet[neighbor] else neighbor

                if indegree[neighbor] == 0:
                    dq.append((neighbor,mostQuietNodeSoFar))
        
        return [track[i] for i in range(len(quiet))]