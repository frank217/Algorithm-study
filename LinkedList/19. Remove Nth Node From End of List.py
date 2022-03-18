'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        result = self.helper(head, n)
        
        if result == 0 :
            return head.next
        
        return head
        
        return rhead
    def helper(self, head: Optional[ListNode], n: int) -> int:
        
        if head.next == None :
            return n - 1
        
        remain = self.helper(head.next,n)
        
        if remain == 0 :
            head.next = head.next.next
        
        return remain-1
        
'''
Solution (Recursion)

Use Recursion to get to last element. remove n until count is Zero. 
If the count is zero that means next needs to be removed. 
Doing so we can handle edge case of removing last element when n = 1.
Also for the case when we need to remove the first element, handle the count in the orignal method.
If First one is removed then we only need return head.next. 

RA : O(N)
SA : O(1)



'''        