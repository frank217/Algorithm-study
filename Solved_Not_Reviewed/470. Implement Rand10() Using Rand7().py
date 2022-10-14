#https://leetcode.com/problems/implement-rand10-using-rand7/


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # 1 2 3 4 5 6 7
        #
        v = 50
        while v > 40 :
            r = rand7()
            c = rand7()
            v = (r-1)*7 + c
        return v%10 + 1        
        