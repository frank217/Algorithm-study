#https://leetcode.com/problems/sum-of-subsequence-widths/

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        #
        nums.sort()
        
        ans, mod,l = 0, 10**9 + 7 , len(nums)
        minv,maxv = 0,0
        for i,n in enumerate(nums):
            maxv = ( maxv + n*pow(2,i, mod))% mod
            minv = ( minv + n*pow(2,l-i-1, mod))%mod
            
            #print(maxv,minv)
        return (maxv-minv) % mod