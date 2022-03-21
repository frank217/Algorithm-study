'''
https://leetcode.com/problems/queens-that-can-attack-the-king/
'''


from collections import defaultdict


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        qdic = defaultdict(set)
        for q in queens:
            qdic[q[0]].add(q[1])
        kr, kc = king[0],king[1]
        for r, c in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
            m = 1
            while r*m+kr >= 0 and r*m+kr < 8 and c*m+kc >= 0 and c*m+kc < 8:
                qr,qc = r*m+kr, c*m+kc
                if  qc in qdic[qr]:
                    res.append([qr,qc])
                    break
                m += 1
        return res


'''
Solution 

Find first queen in all 8 direction.

RA: O(1)
SP: O(1)
'''