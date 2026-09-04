# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_(cur_head):
            prev = None
            while(cur_head):
                nxt = cur_head.next
                cur_head.next = prev
                prev = cur_head
                cur_head = nxt
            return prev
        
        def split_and_reverse(cur_head):
            count = 1
            cur = cur_head

            while(cur and count<k):
                cur = cur.next
                count+=1

            if(not cur):
                return cur_head, None, None

            nxt_head = cur.next
            cur.next = None

            head_ = reverse_(cur_head)
            tail_ = cur_head
            
            return head_, tail_, nxt_head
        
        dummy = ListNode()
        dummy.next = head

        head = dummy
        tail = dummy
        nxt_head = dummy.next

        while(nxt_head):
            head_, tail_, nxt_head = split_and_reverse(nxt_head)
            tail.next = head_
            tail = tail_
        
        return dummy.next