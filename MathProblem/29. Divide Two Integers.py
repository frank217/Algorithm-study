'''
https://leetcode.com/problems/divide-two-integers/
'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        absDividend = abs(dividend)
        absDivisor = abs(divisor)
        signValue = (dividend >= 0) == (divisor >= 0)

        if abs(divisor) == 1:
            result = absDividend if signValue else -absDividend
        else:
            divCount = 0
            while absDividend >= absDivisor:
                i = 1
                curDivisor = absDivisor
                while curDivisor + curDivisor <= absDividend:
                    curDivisor += curDivisor
                    i += i
                absDividend -= curDivisor
                divCount += i
            result = divCount if signValue else -divCount
        
        maxVal = 2**31 -1
        if result > maxVal:
            return maxVal
        minVal = -2**31
        if result < minVal: 
            return minVal
        return result