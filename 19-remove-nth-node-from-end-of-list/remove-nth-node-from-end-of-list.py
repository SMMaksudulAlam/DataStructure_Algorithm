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

        goTill = count-n
        if(goTill==0):
            return head.next

        count = 1
        cur = head

        while(count<goTill):
            cur = cur.next
            count+=1
        
        cur.next = cur.next.next

        return head