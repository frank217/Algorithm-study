'''
https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/
'''


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2 == 1:
            return False
        leftLock = []
        free = []

        for i in range(len(s)):
            if locked[i] == "1" :
                if s[i]=='(' :
                    leftLock.append(i)
                else:
                    if len(leftLock) > 0 :
                        leftLock.pop()
                    elif len(free) > 0:
                        free.pop() 
                    else:
                        return False   
            else:
                free.append(i)
        if len(leftLock) > len(free):
            return False
        for i in range(1,len(leftLock)+1):
            if leftLock[-i] > free[-i]:
                return False
        return True

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2 == 1:
            return False
        free = 0
        for i in range(len(s)):
            if locked[i] == "1" and s[i]==')'  :
                if free > 0:
                    free -= 1
                else:
                    return False
            else:
                free += 1
        free=0
        
        for i in reversed(range(len(s))):
            if locked[i] == "1" and s[i]=='('  :     
                if free > 0:
                    free -= 1
                else:
                    return False
            else:
                free += 1
        return True


'''
Solution 1 
Loop through list ot figure out how many are free to change check for if right parenthesis are valid.
Remove first free for right parenthesis since later index free are used for right parenthesis.
Also caculate how index of left parenthesis that need to be handled.
Check for 

Runtime : O(N)
Space: O(N)


Solution 2
We don't even need to store index. If the left to right works we don't need to consider indexes because only counts need to make sense and it is possible.
Left and right parenthesis should match as long as it is valid and possible.
Runtime : O(N)
space: O(1)

'''commit for fri and sat