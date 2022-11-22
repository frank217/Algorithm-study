# https://leetcode.com/problems/two-city-scheduling/description/


# Bruteforce : Full search TLE 
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:


        def recurse(a,b,i,costs):
            if i == len(costs):
                return 0
            minCost = float("inf")
            if a > 0:
                minCost = min(minCost,recurse(a-1,b,i+1,costs)+costs[i][0])
            if b > 0:
                minCost = min(minCost,recurse(a,b-1,i+1,costs)+costs[i][1])
            return minCost
        
        n = len(costs)//2
        return recurse(n,n,0,costs)

# Solution 1 : 
#   Sort A-B, the lowest value mins chosing B over A is alot more Costly
#   so first half of sorted A-B is going to A and rest to B
        
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        l = []
        for i in range(len(costs)):
            a,b = costs[i]
            l.append((a-b,i))
        
        l.sort(lambda x: x[0])
        n = len(costs)//2
        return sum([costs[i][0] for cost,i in l[:n]]) + sum([costs[i][1] for cost,i in l[n:]])

# Solution 2: 
#   DP solution 
#   dp[i][j] = min cost of i person in City A and j person in City B   
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        n = len(costs)//2
        dp = [[0 for i in range(n+1)]for i in range(n+1)]
        for i in range(n):
            dp[i+1][0] = dp[i][0] + costs[i][0]
            dp[0][i+1] = dp[0][i] + costs[i][1]

        for i in range(n):
            for j in range(n):
                dp[i+1][j+1] = min((dp[i][j+1]+costs[i+j+1][0]),(dp[i+1][j]+costs[i+j+1][1]))
        return dp[n][n]

