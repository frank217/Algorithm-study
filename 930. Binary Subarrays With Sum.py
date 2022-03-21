'''
https://leetcode.com/problems/binary-subarrays-with-sum/
'''
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSumDict = {0:1}
        count = 0
        prefixSum = 0
        for num in nums:
            prefixSum += num
            count += prefixSumDict.get(prefixSum-goal,0)
            if prefixSum not in prefixSumDict:
                prefixSumDict[prefixSum] = 1
            else:
                prefixSumDict[prefixSum] += 1
        return count

'''
Solution (Prefix Sum)
Since array is binary, subarray is always equal or smaller than arary.
Can use moving window to reach sum value and figure how many subarray can be goal sum.
'''