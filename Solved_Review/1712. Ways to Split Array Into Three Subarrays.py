# https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

# Binary Search Question Hard 


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        # sum(left) <= sum(mid) <= sum(right)
        # Non empty list
        # return result % 10**9 + 7
        # nums are all positive.
        
        # Use prefix sum and Binary search to find two index.
        # 1) Create Prefix sum
        # 2) Iterate index where index is end of 1st segment(index i)
        # 3) Use binary search to find end of 2nd segment where (index j)
        #       a) smallest index
        #           condition : prefix[i]*2 <= prefix[j]   
        #           bisect left
        #       b) largest index
        #           condition : prefix[j]-prefix[i] <= prefix[-1] - prefix[j]
        #               =>. prefix[j] <= (prefix[-1]+prefix[i])/2
        #           bisect right
        
        mod, prefix = 10**9 + 7, [nums[0]]
        for i in nums[1:]:
            prefix.append(prefix[-1]+i)
            
        n, cnt = len(nums), 0
        
        for i in range(n):
            ls = prefix[i]
            if ls*3 > prefix[-1]:
                break
                
            a = bisect.bisect_left(prefix,ls*2, i+1)
            tempval = (prefix[-1]+ls)//2
            b = bisect.bisect_right(prefix,tempval,a+1)
            # Need to check 
            #   1) b is not ending index and 
            #   2) bisect return a+1 because there is no such value.  
            if b-1 >= n or prefix[b-1] > tempval : continue
            cnt = (cnt + min(b,n-1)-a) % mod
        return cnt
                
                
        
        
        
        