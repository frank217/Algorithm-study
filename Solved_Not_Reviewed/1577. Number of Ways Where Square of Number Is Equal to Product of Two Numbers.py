#https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 =Counter([n**2 for n in nums1]), Counter([n**2 for n in nums2])
        ans = 0
        for i in range(len(nums1)-1):
            for j in range(i+1, len(nums1)):
                p = nums1[i]*nums1[j]
                if p in n2:
                    #print(i,j,p,n2[p])
                    ans += n2[p] 
        #print("---")
        for i in range(len(nums2)-1):
            for j in range(i+1, len(nums2)):
                p = nums2[i]*nums2[j]
                if nums2[i]*nums2[j] in n1:
                    #print(i,j,p,n1[p])
                    ans += n1[p] 
        return ans
        
        