# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()

        rest = head

        while(rest):
            count = 1
            head = rest
            cur = head
            while(count<k):
                if(not cur.next):
                    if(not dummy.next):
                        return head
                    tail.next = rest
                    return dummy.next

                cur = cur.next
                count+=1
            
            rest = cur.next
            cur.next = None

            prev = None
            cur = head
            
            while(cur):
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            
            if(not dummy.next):
                dummy.next = prev
            else:
                tail.next = prev
            tail = head
            #print("dummy", dummy, "tail", tail, "rest", rest)
        return dummy.next