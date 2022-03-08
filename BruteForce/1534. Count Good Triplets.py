"""
https://leetcode.com/problems/count-good-triplets/


0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
"""

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        r = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if abs(arr[i]-arr[j]) <= a:
                    for k in range(j+1,len(arr)):
                        if abs(arr[k]-arr[j]) <= b and abs(arr[i]-arr[k]) <= c:
                            r += 1
        return r


'''
Solution 1
Brute force solution. Loop through entire search space.

Runtime : O(N^3)
Space : O(1)
'''


