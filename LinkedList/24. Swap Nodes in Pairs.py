'''
https://leetcode.com/problems/swap-nodes-in-pairs/
'''
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        head.next.next = self.swapPairs(head.next.next)
        
        tempHead = head.next
        head.next = tempHead.next
        tempHead.next = head
        
        return tempHead


'''
Solution (recursion)

BaseCase is when head is none or next is none. Nothing to swap.
    - A == None || A.next == None
Recursive case is when Basecase is not met so there are at least two lest fot swap.
Swap the first two, then add the next ones that went through Swap after swaping the first two. 

RA : O(N)
SA : O(1)
'''