# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        cur = head
        while(cur):
            count+=1
            cur = cur.next
        
        half = (count)//2

        dummy = ListNode()
        dummy.next = head
        cur = dummy
        count = 0

        while(count<half):
            cur = cur.next
            count+=1
        return cur.next