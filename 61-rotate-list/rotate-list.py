# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(not head or k==0):
            return head
        
        count = 0
        cur = head
        while(cur):
            count+=1
            cur = cur.next
        
        rotate = k%count

        if(rotate==0):
            return head
        
        rem = count-rotate

        cur = head
        cnt = 1
        while(cnt<rem):
            cur = cur.next
            cnt+=1
        
        nxt = cur.next
        cur.next = None

        cur = nxt
        while(cur and cur.next):
            cur = cur.next

        cur.next = head
        return nxt