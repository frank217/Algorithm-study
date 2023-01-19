# biweekly-contest-93
# https://leetcode.com/contest/biweekly-contest-93/problems/maximum-value-of-a-string-in-an-array/

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        m = -float("inf")
        for st in strs:
            try:
                v = int(st)
            except ValueError:
                v = len(st)
            
            m = max(m,v)
        return m
        