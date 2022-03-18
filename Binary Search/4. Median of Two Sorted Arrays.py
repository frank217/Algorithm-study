'''
https://leetcode.com/problems/median-of-two-sorted-arrays/
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = len(nums1)
        b = len(nums2)
        
        if (a > b):
            return self.findMedianSortedArrays(nums2, nums1)  # Swapping to make A smaller
        
        l, r = 0, a
        h = (a + b +1)//2

        while l <= r :
            mid = (l + r) // 2
            am = mid
            bm = h - mid
            
            # checking overflow of indices
            al = nums1[am  - 1] if (am > 0) else float('-inf')
            ar = nums1[am] if (am < a) else float('inf')
            bl = nums2[bm - 1] if (bm > 0) else float('-inf')
            br = nums2[bm] if (bm < b) else float('inf')

            # if correct partition is done
            if al <= br and bl <= ar:
                if ((a + b) % 2 == 0):
                    return (max(al, bl) + min(ar, br)) / 2.0
                return max(al, bl)

            elif (al > br):
                r = mid - 1
            else:
                l = mid + 1

# This code is contributed by Arpan
'''
Solution 1 
If the list concat doesn't take len of list, then concat two list and sort get median. 


Solution 2
using binary search from longer array and total number get mid for both array 
Lets pick a index in first array.  Given the value can we continually decrease search space?

Lets pick median of first array A as am, how can we find median of both array lies? we need information about second array. 
Get median of second array B as bm. Just be looking at both median we can't figure out median of both array lives. 
Lets also get  value before our median for both array. 

so we have two value from A which are, 
    al, ar = A[am-1], A[am]
Also same for B,
    bl, br = B[bm-1], B[bm]



Now Lets decrease search space. 
    If al > br:
        At least half of A is less than al and At least half of B is less than al.
        at least half of (A+B) is less than al. 
        Need to decrease al value. 

        decrease A search space to half by l = l and r = am
    
    If bl > ar:
        At lease half of A is greater than al and at least half of bl is greater than al.
        at least half of (A+B) is greater than al. 

        Need to increase al value. 

        decrease A search space to half by l = am and r = r

reason we can decrease search space is median mean number of element less than and greater than are equal.
So we can just move mid pointer in the longer list to figure out median. 
 

    If al <= br :
        we know half of A is less than br
        One more we can know is half of B is less than br as well
        So at least half of entire array(A+B) is less then br.
        This also means
        Half of B is greater than al and half of A is greater than or equal to al.
        Meaning at least half of entire array(A+B) greater than al. 

    If bl <= ar : 
        Half of A is less than  ar
        We also know half of B is less than ar as well.  
        meaning At least half of entire array (A+B) is less than ar.
        This also means
        Half of B is greater to bl and half of A is greater than bl.
        Meaning at least half of entire array(A+B) is  greater than bl. 

    If both is true we get an answer. 
        At least half of entire array(A+B) is less then br and at least half of entire array(A+B) is  greater than bl. 
        So either bl and br has to be median of the given array
        Same for array A, al and ar has to be median of the given array.
        We need to figure out true median among this four value which can be done have 
        If len(A) + len(B) is even:
            (max(al,bl) + min(ar,br))/2 = average of max of lesser two and min of greater two = median
        if odd :
            It will be either be max of lesser two or min of greater two depending on the implementation. 
            We are going to use max of lesser two.








1)   

'''