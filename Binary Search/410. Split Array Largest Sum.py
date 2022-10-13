#https://leetcode.com/problems/split-array-largest-sum/

# Binary Search Problem
 # Also  Called as Parametric Search 
 #  Parametric Search transforms Decision Algorithm into Optimization Algorithm
 #  Meaning it transform Yes, No question into finding best solution. 

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Binary Search
        # Problem is to find value where it is possible to split nums in to m section
        # Use Binary Search on this value to get smallest possible value for this
        # Smallest possible value is max vavlue in nums and sum of Nums is Highest value if only one value in nums
        
        l,h = max(nums), sum(nums)
        
        while l < h:
            mid = (l+h)//2 
            segmentSum,cnt = 0,1
            
            for num in nums:
                if segmentSum + num <= mid:
                    segmentSum += num
                else:
                    cnt += 1
                    segmentSum = num
            if cnt > m :
                l = mid + 1
            else:
                h = mid
        return h
                    
                
             