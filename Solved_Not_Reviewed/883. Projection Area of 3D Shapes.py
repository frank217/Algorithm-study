#https://leetcode.com/problems/projection-area-of-3d-shapes/

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        # Get xy 
        
        xy = 0
        for r in grid:
            for c in r:
                if c != 0:
                    xy +=1
        xz = 0
        for r in grid:
            xz += max(r)
        
        yz = 0
        for i in range(len(grid[0])):
            col = [ r[i] for r in grid]
            yz += max(col)
        
        return xy + xz + yz