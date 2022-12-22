# weekly-contest-324
# https://leetcode.com/contest/weekly-contest-324/problems/cycle-length-queries-in-a-tree/


class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
#                   1 1
#               2 10.                             3 11
#       4 100        5 101                  6 110         7 111
# 8 1000  9 1001  10 1010  11 1011  12 1100  13 1101  14 1110  15 1111     

        # convert check diff index
        ans = []
        for a,b in queries:
            bina = bin(a)[2:]
            binb = bin(b)[2:]
            
            i = 0
            while i <len(bina) and i < len(binb):
                if bina[i] != binb[i]:
                    break
                i += 1
            
            ans.append(len(bina)-i + len(binb)-i +1)
        return ans
                