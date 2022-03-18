'''
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
'''

import math


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        remain = self.helper(head,1)
        
        if remain == 0 :
            return head.next
        
        return head
    
    def helper(self, head: Optional[ListNode], n: int) -> int:
        if head.next == None:
            
            return math.ceil(n/2)-1
        
        remain = self.helper(head.next, n+1)
        
        if remain== 0:
            head.next = head.next.next
        
        return remain - 1

'''
Solution (recursion)

BaseCase: If there are no more next, find the midvalue and return 
RecursiveCase : Increase the counter and recurse until base case. Then with the midvalue found from basecase, 
check if the next node is middle node, and remove if so. 
Decrease the counter and return.

RA : O(N)
S: O(1)

'''