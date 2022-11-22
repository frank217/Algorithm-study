class Solution:
    def numberOfWays(self, s: str) -> int:
        # DP : Given 
        # for ith index and j for chosen number 
        # DP[i][select] = Sum of j index before i and select-1 and str[i] != str[j]

        dp = [[0 for i in range(len(s))] for j in range(3)]
        
        for i in range(len(s)):
            dp[0][i] = 1
            b = s[i]
            for j in range(i):
                prevb = s[j]
                if prevb != b:
                    dp[1][i] += dp[0][j]
                    dp[2][i] += dp[1][j]
        #print(dp) 
        return sum(dp[2])

        
        # DP with one time rurn
        # answer is either 010 or 101
        # 
        zero, one  = 0,0
        IO, OI = 0,0
        ans = 0

        for ch in s:
            if ch == "0":
                zero += 1
                IO += one
                ans += OI
            else:
                one +=1
                OI += zero
                ans += IO
        return ans

