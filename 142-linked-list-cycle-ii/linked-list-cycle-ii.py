# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):
            return None
        
        slow = head
        fast = head

        if(not fast.next):
            return None

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if(not fast or not fast.next):
                return None
            if(fast == slow):
                break
        
        cur = head

        while(cur!=slow):
            cur = cur.next
            slow = slow.next
        return cur

        
