'''
https://leetcode.com/problems/rectangle-area/submissions/
'''


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        aArea = (ax2-ax1) * (ay2-ay1)
        bArea = (bx2-bx1) * (by2-by1)

        xl = max(ax1,bx1)
        xr = min(ax2,bx2)
        yl = max(ay1,by1)
        yr = min(ay2,by2)
        
        if xr > xl and yr > yl:
            #Compute intersection
            iArea = (xr-xl) * (yr-yl)
            return aArea + bArea-iArea
        
        return aArea + bArea 


'''
Solution

Caculate the Insertection. If there is intersection minus the intersection from sum of two area.
'''