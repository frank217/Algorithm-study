'''
https://leetcode.com/problems/3sum/
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        r = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            
            jkSum =  - nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] < jkSum:
                    j += 1
                elif nums[j] + nums[k] > jkSum:
                    k -= 1
                else:
                    r.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while nums[j-1] == nums[j] and j < k:
                        j += 1
        return r

'''
Solution

Given we need to find 3 distinct values that makes up 0, we need to sort the given list to easily handle duplicates.
nums[i] + nums[j] + nums[k] = 0   =>  nums[j] + nums[k] = -nums[i]

given nums[i] is static we can find nums[j] + nums[k] by using moving windows. Reason for using moving windows is it easy to opt out deplicates during 
search and it only take O(len(Num)) = O(N) to search for it. 

Moving Window is relatively simple to implement with condition and we don't want to count in same number. 
If the num[i-1] == num[i]  or num[j-1] == num[j] skip it from caculation.
K is ignored because if I and J doesn't count duplicates regardless of nums[k] value, nums[i],nums[j],nums[k] will be unique


Runtime: O(N^2)
Sort is O(NlogN) + nested loop with moving window O(N) * O(2N) = O(NlogN) + O(N^2) = O(N^2)

Space: O(N) for newly sorted list.
'''