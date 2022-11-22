#https://leetcode.com/problems/matrix-cells-in-distance-order/description/
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        
        dq = deque([(rCenter,cCenter)])
        visited =set([(rCenter,cCenter)])
        ans = []
        while dq:
            r,c = dq.popleft()
            ans.append((r,c))
            neighbor = []
            if r > 0 :
                neighbor.append((r-1,c))    
            if c > 0 :
                neighbor.append((r,c-1))
            if r < rows-1:
                neighbor.append((r+1,c))
            if c < cols-1:
                neighbor.append((r,c+1))
            for n in neighbor:
                if n not in visited:
                    dq.append(n)
                    visited.add(n)
        return ans
            
            
