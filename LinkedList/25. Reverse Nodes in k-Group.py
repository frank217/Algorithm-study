'''
https://leetcode.com/problems/reverse-nodes-in-k-group/
'''
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        returnHead,t = self.ReverseHelper(head,k)

        while t!=None and t.next != None:
            nextH, nextT =  self.ReverseHelper(t.next,k)
            t.next = nextH
            t = nextT
            
        return returnHead
        
    def ReverseHelper(self,head: Optional[ListNode], k: int) -> ( Optional[ListNode], Optional[ListNode]):
        
        if k == 1:
            return (head,head)    
        
        if head.next == None:
            return (head,None)
        
        h,t = self.ReverseHelper(head.next,k-1)
        
        if t== None:
            return (head,t)
        
        head.next = t.next
        t.next = head
        
        return (h,head)


'''
Solution (Recursion)

Require method. 
First for reversing every K element
Second for iterating First method until end has been reached. 


First method(Recursion)
Given head and value K, reverse first K values. 

Base Case : 
    1)  If reach end of the list with out reaching Kth element return head and None, since tail is None now. 
    2)  If reach Kth node is reached start return current node and head and tail. 

Recursive Case :
    1) If tail is none, don't reverse and return current head and Tail, which is None.
    2) If not, current head need to be inserted after tail to reverse the order. 
        Attach tail.next to current head's next.
        Attach current head to tail.next
        return head from recursive case and current head as tail.

Second Method.
Given a list and Value K reverse every Kth elements in the list.

Since we need to return the head, run the first Method on first Kth node. 
It will return head whether it is reversed or not. Keep the head for result. 
tail will be used to link to next iteration. 
Run the first method until tail is None or next of tail is none we. In this case don't need to perform reverse anytmore.
Once the frist method run we till get next head and next tail. 
link tail.next to next head and assign next tail to current tail. 
return the first head we got and return it. 

RA : O(N)
    Fairly straight forward. Only need to run 2* N amount for this implementation. which is O(N)
SA : O(1)

'''