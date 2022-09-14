# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

# Greedy Problem


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # Linear Greedy problem. 
        seat,plant = 0, 0
        MOD,res = 10**9+7, 1
        
        for i in corridor:
            if i == "S":
                if seat < 2:
                    seat += 1
                else:
                    res = (res * (plant+1)) % MOD
                    seat = 1
                    plant = 0
            else:
                if seat == 2:
                    plant += 1
        if seat == 0:
            return 0
        if seat == 1:
            return 0
        
        return res
        