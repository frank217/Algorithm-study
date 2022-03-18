'''
https://leetcode.com/problems/longest-palindromic-substring/
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for i in range(len(s))]
        maxV = 0
        mi,mj = 0,0
        for wordLength in range(1,len(s)+1):
            for i in range(len(s)-wordLength+1):
                j = i + wordLength -1 
                
                if i == j :
                    dp[i][j] = True
                else:                    
                    if s[i] == s[j]:
                        if i+1 == j:
                            dp[i][j]  = True
                        else:
                            dp[i][j]  = dp[i+1][j-1]
                    else: 
                        dp[i][j]  = False
                if dp[i][j] and wordLength > maxV:
                    maxV = wordLength
                    mi,mj = i,j

        return s[mi:mj+1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ss = ''
        for i in range(len(s)): ss = max(self.checkPalindrom(s, i, i), self.checkPalindrom(s, i, i + 1), ss, key=len)
        return ss
    
    def checkPalindrom(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]: l -= 1; r += 1
        return s[l+1:r]



'''
Solution 1
Simple DP.

Base Case 
    Dp[i][j] where i == j  if s[i] == s[j] then palindrome else not. 
    Dp[i][j] where i+1 == j  if s[i] == s[j] then palindrome else not. 

Recursive Case    
    DP[i][j] = if s[i] == s[j] and Dp[i][j] then palindrome.

Runtime : O(N^2)
Space :   O(N^2)


Solution 2
Use Center of Palinedrome
There are 2n-1 center of Palindrome. Because of odd and even length
For each center expand out untill paline is no longer true.
2n-1 * n operations required.

Runtime : O(N^2)
Space : O(1)
'''