# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next and head.next.next):
            return head
        root = odd = head
        even = ListNode()
        eve = even
        while odd and odd.next and odd.next.next:
            even.next = odd.next
            odd.next = odd.next.next
            odd = odd.next
            even = even.next
            if odd and odd.next and not odd.next.next:
                even.next = odd.next
                even = even.next
        even.next = None
        odd.next = eve.next
        return root

        