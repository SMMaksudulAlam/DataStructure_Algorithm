# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = head
        while(cur):
            count+=1
            cur = cur.next
        
        gotill = count-n
        if(gotill == 0):
            return head.next

        dummy = ListNode()
        dummy.next = head

        cur = dummy
        count = 0

        while(count<gotill):
            cur = cur.next
            count+=1
        
        cur.next = cur.next.next

        return head