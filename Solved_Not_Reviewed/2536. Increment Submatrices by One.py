# Medium
# https://leetcode.com/contest/weekly-contest-328/problems/increment-submatrices-by-one/

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        m = [[0 for i in range(n)] for i in range(n)]

        for r1,c1,r2,c2 in queries:
            for r in range(r1,r2+1):
                m[r][c1] += 1
                if c2 < n-1:
                    m[r][c2+1] -= 1
        
        for r in range(n):
            for c in range(1,n):
                m[r][c] += m[r][c-1]

        return m
            