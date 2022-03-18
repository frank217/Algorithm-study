'''
https://leetcode.com/problems/generate-parentheses/
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dic = {}
        return self.helper(n,n)

        
    def helper(self, l:int,r:int) -> List[str]:

        if l == 0 and r ==0:
            return [""]

        result = []
        if l > 0 :
            lResult = self.helper(l-1,r)
            for lr in lResult:
                result.append("(" + lr)
        if r > l :
            rResult = self.helper(l,r-1)
            for rr in rResult:
                result.append(")"+rr)


        return list(dict.fromkeys(result))



'''
Solution
Backtracking possible solutions.
1) Count possible remaining left and right parenthesis.
2) For Left parenthesis if remain remove count and backtrack
3) For Right parenthesis if number of right parenthesis is greater than left remove count and backtrack
4) Base case if no remant remain return empty list. 

runtime : O(2^N)
Space : O(2^N)

'''