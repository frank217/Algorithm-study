# weekly-contest-324
# https://leetcode.com/contest/weekly-contest-324/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        def getPrimeFactors(num):
            res = []
            while num % 2 == 0:
                num /= 2
                res.append(2)
            
            for i in range(3,int(math.sqrt(num))+1,2):
                while num % i == 0 :
                    num /= i
                    res.append(i)
            if num >2 :
                res.append(int(num))
            return res
        
        
        res = getPrimeFactors(n)
        while len(res) > 1:
            newn = sum(res)
            if newn == n :
                return n
            n = newn
            res = getPrimeFactors(n)
        return res[0]