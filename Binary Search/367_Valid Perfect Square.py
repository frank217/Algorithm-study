"""
From LeetCode
https://leetcode.com/problems/valid-perfect-square/

367. Valid Perfect Square - Easy 

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1
"""

import math


class Solution1(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ans = 1
        while ans**2 < num :
            ans += 1
        
        return ans**2 == num

class Solution1(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 1
        r = num
        
        while (l <= r):
            mid = l + (r-l) // 2
            if mid*mid == num:
                return True
            elif mid * mid < num:
                l = mid + 1
            else:
                r = mid - 1
            
        return False

"""
Solution

Need to figure out if num is sqrt of any positive integer. 

solution 1  O(sqrt(N))
Given we have started with smallest positive number 1, refer as A and our given number as Num.
Since A started with smallest positive number 1 and 1 <= num <= 2^31 - 1
Case 1: If Num is not greater square of A, Num is either Equal to Square of A or not a perfect square because  A^2 >= Num.
Case 2: If Num is greater square of A, increase A. 
Repeat until Case 1 is reached.


solution 2  O(log(n))
Can run Binary Search on the Num to figure out which number is either smae or larger than Num
Need to write up a good Explanation for Binary Search. 
"""        