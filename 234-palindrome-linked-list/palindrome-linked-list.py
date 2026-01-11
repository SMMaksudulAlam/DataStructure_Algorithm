# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        count = 0
        cur = head

        while(cur):
            count+=1
            cur = cur.next
        
        half = count//2

        dummy = ListNode()
        dummy.next = head
        cnt = 0

        prev = None
        cur = dummy

        while(cnt<half+1):
            cnt+=1
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

        if(count%2==1):
            cur = cur.next

        while(cur):
            if(cur.val != prev.val):
                return False
            cur = cur.next
            prev = prev.next
        return True
        


