'''
https://leetcode.com/problems/valid-parenthesis-string/
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        free = 0
        for i in s:
            if i == ')':
                if free> 0:
                    free -= 1
                else:
                    return False
            else:
                free += 1
        free=0
        for i in reversed(s):
            if i =='(':
                if free> 0:
                    free -= 1
                else:
                    return False
            else:
                free += 1
        return True
            