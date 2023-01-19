# Medium
# https://leetcode.com/contest/weekly-contest-328/problems/count-the-number-of-good-subarrays/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # moving windows
        l,r,curPair = 0,0,0
        cnt = defaultdict(int)
        
        ans = 0
        while l < len(nums):
            while r < len(nums) and curPair < k:
                v = nums[r]
                curPair += cnt[v]
                cnt[nums[r]] +=1
                r += 1
            if curPair >= k:
                ans += len(nums) - r + 1
                
            curPair -= cnt[nums[l]]-1
            cnt[nums[l]] -= 1
            l += 1
        
        return ans
    
# [2,1,3,1,2,2,3,3,2,2,1,1,1,3,1]
#        1 1 2 1 2 3
#          2 4 5 7 10
# 11