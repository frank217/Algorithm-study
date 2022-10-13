#https://leetcode.com/problems/fraction-to-recurring-decimal/

class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if n == 0 : return "0"
        
        ans =""
        if (n > 0) ^ (d > 0) :
            ans += "-"
            n = abs(n)
            d = abs(d)
        elif n < 0 and d < 0:
            n = abs(n)
            d = abs(d)
        
        ans += str(n//d)
        n = n%d
        
        if n == 0 : 
            return ans
        else: 
            ans += "."
        
        s = {}
        maxlen = 10**4
        while n!=0 and len(ans) < maxlen:
            print(ans,n)
            n *= 10 
            if n not in s: 
                s[n] = len(ans)
            else:
                ans = ans[:s[n]] + "(" + ans[s[n]:] + ")"
                return ans
            ans += str(n//d)
            n = n%d
            
        return ans
            
            
            
            
        