#https://leetcode.com/problems/score-after-flipping-matrix/


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        #Greedy : 
        # 1. left column being 1 is always best. Change first column to be 1
        # 2. Then check each column to contain most 1s.
        r , c = len(grid),len(grid[0])
        for ri in range(r):
            if grid[ri][0] != 1:
                grid[ri] = [ 0 if x == 1 else 1 for x in grid[ri]]
        
        colhalf = r/2
        for ci in range(c):
            if sum([row[ci] for row in grid]) < colhalf:
                for row in grid:
                    row[ci] = 0 if row[ci] == 1 else 1
        ans = 0
        for row in grid:
            ans += int(''.join(map(str,row)),2)
        return ans
        