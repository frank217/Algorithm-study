#https://leetcode.com/problems/course-schedule/

# Graph problem (topological sort)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Just need to check if there are any circular loop.
        # Run Topological sort and the node that aren't pushed to que is circular looped nodes.
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for p in prerequisites:
            graph[p[0]].append(p[1])
            indegree[p[1]] += 1
        
        rootNode = set([i for i in range(numCourses)]).difference(set(indegree.keys()))
        
        dq = deque(rootNode)
        visited = set()
        while dq:
            node = dq.popleft()
            visited.add(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0 :
                    dq.append(neighbor)
        return len(visited) == numCourses
            
        
        
        