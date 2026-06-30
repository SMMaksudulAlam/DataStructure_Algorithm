# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(not head):
            return False

        slow = head
        fast = head.next
        if(not fast):
            return False
        else:
            fast = head.next

        while(fast!=slow):
            if(not fast):
                return False
            slow = slow.next
            fast = fast.next
            if(fast):
                fast = fast.next
        
        return True