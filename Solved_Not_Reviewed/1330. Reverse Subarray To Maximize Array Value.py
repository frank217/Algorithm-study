#https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/



# Explanations 
#  https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/discuss/489882/O(n)-Solution-with-explanation
class Solution:
    def maxValueAfterReverse(self, A: List[int]) -> int:
        # 1. absolute diff of i and i+1
        # maximize by reversing subarray
        # what does reversing subarray do?
        
        # Reverse will only take effect on each end of reversal since give x,y  abs(x-y) = abs(y-x)
        # given array where  [... a, {b ... c},d...] and reverse happends on b,c.
        # diff will be  - (abs(a-b) + abs(c-d)) + (abs(a-c) +  abs(b-d))
        # how do we max this value.

        # 

        total, res, min2, max2 = 0, 0, float('inf'), -float('inf')
        #print(zip(A, A[1:]))
        for a, b in zip(A, A[1:]):
            total += abs(a - b)
            res = max(res, abs(A[0] - b) - abs(a - b))
            res = max(res, abs(A[-1] - a) - abs(a - b))
            min2, max2 = min(min2, max(a, b)), max(max2, min(a, b))
        return total + max(res, (max2 - min2) * 2)
        