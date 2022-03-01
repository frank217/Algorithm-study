'''
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
'''

class Solution1(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rn = len(matrix)
        cn = len(matrix[0])
        
        for i in range(rn):
            l = 0 
            h = cn-1
        
            while l <= h :
                mid = (l+h)//2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    l = mid+1
                else: 
                    h = mid-1
        return False

'''
Solution 1
Use Binary Search on each row to find where possible target might be

Runtime : O(Row*log(Col))
Space : O(1)

Improvement:
Can use binarysearch if Row > Col
'''

class Solution2(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rn = len(matrix)
        cn = len(matrix[0])
        
        r = 0
        c = cn-1 
        while r < rn and c >= 0 :
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            else: 
                c -= 1 
        return False

'''
Solution 2
Need to run Binary Search on Row and Column. The Row and Column are monotonic. It is always increasing with higher index. 
In order to perform Binary Search and remove search space, either the Row or column needs to start at opposite end.
Choosing row and low and column as high. Mid is going to be Matric[Row][Column] because we can start reducing search space by
moving Row or column. 

Init value : Row = 0 and Column = column length
If Matrix[Row][Column] == target
Found asnwer
If Matrix[Row][Column] < target
Any value in this row doesn't have the target. Because we used max value in this row.
Increase row value to find possible target. 
If Matrix[Row][Column] > target
Decrease column to find possible target. Reason we can do this is we are at row zero and and value in other row for this column will be greate thus 
we can safely remove them from search. 

With Same reason on the second run we continue to decrease the search space until we find the target value.
If we have read max row and min column that means there is no more search space left and therefore target value is not in matrix.

Runtime : O(Row+Column)
Space : O(1)

'''