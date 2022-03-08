'''
https://leetcode.com/problems/3sum-closest/
'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestV = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i] :
                continue
            
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                #print(sum3, closestV)

                if abs(target-closestV) > abs(target-sum3):
                    closestV = sum3
                if sum3 < target : 
                    j += 1
                elif sum3 > target : 
                    k -= 1
                else:
                    return sum3

                
        return closestV


'''


'''