# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

# Greedy Problem


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # Linear Greedy problem. 
        cnt,Mod = 0, 10**9 + 7
        seat,plant = 0,0
        
        for v in corridor:
            if v == "S":
                if seat == 2:
                    cnt = (max(cnt,1) * (plant+1)) % Mod
                    seat = 1
                    plant = 0
                else:
                    seat += 1
            else:
                if seat ==2:
                    plant +=1
        
        if seat == 2:
            return max(cnt,1)
        
        return 0
        