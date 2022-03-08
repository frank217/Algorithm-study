'''
https://leetcode.com/problems/count-special-quadruplets/
'''
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        i1 = 0
        i2 = 1
        i3 = 2
        s = 3
        r = 0
        while i1 < len(nums)-3:
            
            while i2 < len(nums)-2:
                i12 = nums[i1] + nums[i2]
                while i3 < len(nums)-1 : 
                    i123 = i12 + nums[i3]
                    while s < len(nums):
                        if i123 == nums[s]:
                            r+=1
                        s +=1
                    i3 +=1
                    s = i3 + 1
                i2+=1
                i3 = i2 + 1
                s = i3 + 1
            i1 += 1
            i2 = i1 +1
            i3 = i2 +1
            s = i3 +1
        return r


'''
Solution 1

Search entire search space to find result.

TimeAnalysis : O(N^4)
Sapce : O(1)
'''


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        abSum= {}
        r = 0

        for b in range(1,len(nums)-2):
            for a in range(0,b):
                sum = nums[a]+nums[b]
                abSum[sum] = abSum.get(nums[a]+nums[b],0) + 1
            for d in range(b+2,len(nums)):
                diff = nums[d] - nums[b+1]
                r += abSum.get(diff, 0)
        return r
'''
Soution 2

If we convert a+b+c = d then a+ b = d-c. With condition a<b<c<d.
If we have all the value a +b caculate for values less than c, we can get how many value are d-c previous to C. 
as we increase b from 1 to len(nums)-2, d-c can be caculated with c being b+1 and from b+2 to len(nums).

for b from 1 to len(nums)-2
    1) Caculate apperance of value a+b in dictionary
    2) since we now all the appreances of sums in dictionary all, given c = b+1 find how many d-c occured previously dictionary and count it in.

Runtime : O(N^2)
    Since we only loop through double nested for loop that both does not exceed len(nums) it is less than N^2. 
    To be precise (1+2+....n-3) + (n-3 ... + 2 + 1) = ((n-2)^2)/2 + ((n-2)^2)/2 = (n-2)^2.  => O(n^2)
Space : O(N^2)
    Since we are storing sum of a + b. If sum of a + b is all different number, Possible sume combination is (N-3) * (N-3) => O(N^2)

'''