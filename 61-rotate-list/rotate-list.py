# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(not head):
            return head
        len = 0
        cur = head
        while(cur):
            cur = cur.next
            len+=1
        
        k = k%len
        if(k==0):
            return head

        prev = None
        cur = head
        while(cur):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        newHead = prev
        count = 1
        prev = None
        cur = newHead
        tempTail = newHead
        while(count<=k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count+=1

        res = prev
        prev = None
        while(cur):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        tempTail.next = prev
    
        return res
    
        
