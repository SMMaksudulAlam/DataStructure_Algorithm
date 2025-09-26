# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        cur = dummy_head
        carry = 0

        while(l1 and l2):
            s = l1.val + l2.val + carry
            nde = ListNode(s%10)
            carry = s//10
            cur.next = nde

            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        while(l1):
            s = l1.val + carry
            nde = ListNode(s%10)
            carry = s//10
            cur.next = nde

            cur = cur.next
            l1 = l1.next

        while(l2):
            s = l2.val + carry
            nde = ListNode(s%10)
            carry = s//10
            cur.next = nde

            cur = cur.next
            l2 = l2.next

        if(carry):
            nde = ListNode(carry)
            cur.next = nde
        
        return dummy_head.next



             