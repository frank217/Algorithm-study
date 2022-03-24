
'''

'''


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return -1 if k%2 else nums[0]

        if k <= 1 :
            return nums[k]        
        if n < k :
            return max(nums)

        r = max(nums[:k-1])
        if n > k:
            r = max(nums[k], r)
        return r

'''
Solving EdgeCases

If list has only one value, we can only add or insert the value depending on the k.
If odd can only remove and on even can only insert. As a result the return -1 if odd and first num if even.

If list has more than one then what we can return depend on the length of list and k. 
If k is 0 or 1 we can only return first or second element. becasue we only have option to not do anything or remove.
Else if length of list is less than k we can remove all and only insert the maxvalue on given kth moment. 
Else if the length of list is greater than K we can we have condition on the last move. 
we can either remove the element or insert what we have so far. So we can get max of first K-1 nums in list and number after K.
But if the length of list equal K then we only have option to insert. So in that case just return K-1 



'''        