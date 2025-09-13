# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        cur = node
        while(list1 and list2):
            v1 = list1.val
            v2 = list2.val

            if(v1<=v2):
                cur.next = list1
                list1 = list1.next
                cur = cur.next
                cur.next = None
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next
                cur.next = None
        
        if(list1):
            cur.next = list1
        if(list2):
            cur.next = list2
        
        return node.next