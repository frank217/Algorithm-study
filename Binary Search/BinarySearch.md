# Binary Search

Given a array or list find a value by decreasing search space by half every time. 
Condition for using binary search is that list is ordered or monotonically increasing or decreaing. 

Runtime Analysis : O(log(N))
Generaly runs in O(log(N)) given the length of array N.
Upper bound being the maximum number of Search required. logN is max number of iteration required since 
we are decreasing the search space by half everytime.
Lower bound being one time search.
Further Runtime Analysis may vary depending on the implementation. 

Space Analysis : O(1)
Since we only need high and low index to continue the search space required for this algorithm is constant. 


Example) python 3
Given array arr of size n, find index of value k and if not present return -1.
def binarysearch(self, arr, n, k):
    l = 0
    h = n-1

    while l <= h:
        m = (l + h)//2
        if arr[m] == k :
            return m
        elif arr[m] < k :
            l = m+1
        else: 
            h = m-1
    return -1

Explanation:
Search need to happend bewteen first and last index. 
There are three cases for the search. 
1) If the middle value = K. Return middle index.
2) If the middle value < K. Search values above middle index. (l = m+1)
3) If the middle value > K. Search value below middle index.  (h = m-1)

What if the value isn't in the array? What is ending condition
If there is only one left, l = mid = h so we would know it whether we found the value or not.
If not it would either perform 2) or 3) and l <= h will no longer be true.

If there are two left,  l = mid = h -1. 
If mid is not the value we want it will converge to only one left.

If ther are three left l +1 = mid = h-1.
If mid is not the value we want it will converge to only one left.

going forward it is recursive process. 
