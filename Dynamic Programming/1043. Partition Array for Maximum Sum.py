'''
From Leetcode
https://leetcode.com/problems/partition-array-for-maximum-sum/
'''

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0]* len(arr)
        m = 0
        
        
        for i in range(len(arr)):
            if i < k:
                m = max(m,arr[i])
                dp[i] = m * (i+1)
            else:
                m = 0 
                for j in range(0,k):
                    m = max(m, arr[i-j])
                    tempMax = dp[i-j-1] + (j+1)*m
                    dp[i] =  max(dp[i],tempMax)
        return dp[-1]
        
            
'''
Solution 
Naive solution would be to repetitively caculate value for all possible partitioning.
Since naive solution require multiple iteration, DP would best fit solution to decrease its runtime.
Given an index, if we know max possible value for all the previous index, we can caculate max value for
current index by looping through previous k index(inclusive). 
CurrentMaxValue = Max(K previous value) * k + previousMaxValue  

Base case:
For the first K element, Max output is Max(first K value) * K 
Dp[i] = Max(previous k value arr[i] inclusive) * k ; k = 1,2 ... K
Induction:
DP[i] = DP[i-k] + Max(previous k value arr[i] inclusive) * k ; k = 1,2 ... K


Runtime : O(nK)
n = len(arr)

Space : O(n)
For DP memory
'''        