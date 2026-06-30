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
        fast = head

        while(True):
            if(not fast):
                return False
            slow = slow.next
            fast = fast.next
            if(fast):
                fast = fast.next
            if(fast and slow == fast):
                return True
        return False