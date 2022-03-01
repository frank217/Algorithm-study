'''
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rn = len(matrix)
        cn = len(matrix[0])
        l = 0
        h = rn * cn - 1 
        
        while l <= h :
            mid = (l+h)//2
            r= mid//cn
            c= mid%cn
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                l = mid+1
            else: 
                h = mid-1
        return False

'''

Solution 1 (not implemented)
Use Modified Binary Search on row first to find where possible target might be
Then use Binary Search to on that row to find target.

Runtime : O(log(Row)+log(Column)) => O(log(Row*Column))
Space : O(1)


Solution 2:
Use binary Search as if the value matrix is linear.
everytime recaulate row and column index to from mid value to find the target.

Runtime : O(log(Row*Column))
Space : O(1)
'''