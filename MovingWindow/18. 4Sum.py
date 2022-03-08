'''
https://leetcode.com/problems/4sum/
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        print (nums)
        dic = {}
        res =[]
        
        for a in range(len(nums)-3):
            if a > 0 and nums[a-1] == nums[a]:
                continue
                
            bcdSum = target-nums[a]
            for b in range(a+1,len(nums)-2):
                if b > a+1 and nums[b-1] == nums[b]:
                    continue
                cdSum = bcdSum - nums[b]
                    
                c = b + 1
                d = len(nums) - 1 
                while c < d : 
                    if nums[c] + nums[d] < cdSum:
                        c += 1
                    elif nums[c] + nums[d] > cdSum:
                        d -= 1
                    else: 
                        res.append([nums[a],nums[b],nums[c],nums[d]])
                        c += 1
                        while nums[c-1] == nums[c] and c < d:
                            c += 1 
        return res

'''
Solution 

Extended Version of Sum of 3 question. Just use another forloop over Sum  of 3 question and solve. 

'''