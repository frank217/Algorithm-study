'''
https://leetcode.com/problems/maximum-score-from-removing-stones/
'''
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        l = [a,b,c]
        l.sort()
        r = 0
        while l[1]> 0:
            r += 1
            l[2] -= 1
            l[1] -= 1
            l.sort()
        return r
        