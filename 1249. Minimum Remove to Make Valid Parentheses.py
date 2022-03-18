'''
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/s
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l = 0
        
        result = ""
        for i in s:
            if i == '(':
                l += 1
            elif i==')':
                if l > 0 :
                    l -=1
                else:
                    continue 
            
            result += i
        result1 = ""
        if l > 0 :
            for i in reversed(result):
                if i == '(' and l > 0:
                    l -= 1
                    continue
                result1 = i + result1
                
        else:
            return result
                
        return result1
            