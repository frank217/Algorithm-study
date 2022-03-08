'''
https://leetcode.com/problems/rotate-image/
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        #transpose
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] =  matrix[j][i],matrix[i][j]

        # Reverse row
        for r in range(n):
            matrix[r] = matrix[r][::-1]
        return matrix

'''
Solution

Math problem. Transpose matrix and reverse the column order to rotate 90 degree

Runtime : O(n^2)
Space : O(1)
'''        