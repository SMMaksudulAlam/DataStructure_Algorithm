# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):
            return None
        left1 = head
        left2 = head.next

        while(left2 and left2.next):
            right2 = left2.next
            left2.next = left2.next.next
            left2 = left2.next

            right1 = left1.next
            right2.next = right1
            left1.next = right2
            left1 = left1.next

        return head





            