'''
1394. Find Lucky Integer in an Array


https://leetcode.com/problems/find-lucky-integer-in-an-array/



'''


class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dict = {}
        maxVal = -1
        for i in arr:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for i in dict:
            if dict[i] == i:
                maxVal = max(i,maxVal)
        return maxVal

'''
runtime : O(N)
Space   : O(N)

Use Dictionary to track count of each number and find if the number and the count match.\
Also Keep track of the largest value as well
'''