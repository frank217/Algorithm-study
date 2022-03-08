'''
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

Similar to 48.

'''
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        n = len(mat)
        rotate = 0
        while rotate < 3:
            for r in range(n):
                for c in range(r+1,n):
                    mat[r][c], mat[c][r] = mat[c][r],mat[r][c]
        
            for i in range(n):
                mat[i] = mat[i][::-1]
            if mat == target:
                return True
            rotate +=1
        return False

'''
Solution

Math problem. Transpose matrix and reverse the column order to rotate 90 degree
Try it 3 times to check if rotating will get target matrix.

Runtime : O(n^2) *3
Space : O(1)
'''