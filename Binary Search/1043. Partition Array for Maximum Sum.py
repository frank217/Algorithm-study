'''
From Leetcode
https://leetcode.com/problems/partition-array-for-maximum-sum/




'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1

        while l < h : 
            print (l,h)
            mid = (l + h)//2
            if nums[mid] == nums[h] :
                h -= 1
            elif nums[mid] < nums[h] :
                h = mid
            else :  
                l = mid + 1
        
        return nums[l]


'''
Solution 

Use Binarysearch to find min value.
For a given mid value there can be multiple state.
1) No rotation monotonically increaseing 
    technically return first value 
2) Rotation ocurred where duplicates causing finding mid. 
    a) mid < high : high = mid  because mid can be answer. 
    b) low > mid : low = mid + 1
3) Rotation wher first and last value are same due to duplicates.
    Due to this case when we are searching for value if l = h, need to decrease h until l != h

Runtime : 
upper bound being O(N)
Lower bound being O(log(N))



Space   : O(1)



'''        