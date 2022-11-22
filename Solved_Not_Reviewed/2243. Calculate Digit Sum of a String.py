# https://leetcode.com/problems/calculate-digit-sum-of-a-string/description/
# Easy
#11/09/22

class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            # Do one round
            newS = ""
            while s:
                group = s[:k]
                s = s[k:]
                sumS = 0 
                for i in group:
                    sumS += int(i)
                newS += str(sumS)
            s = newS
        return s
            