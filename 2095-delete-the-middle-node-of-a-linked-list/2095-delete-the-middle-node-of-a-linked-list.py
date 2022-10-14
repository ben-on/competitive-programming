# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=0
        root=root2=ListNode(0,head)
        while head:
            l+=1
            head=head.next
        l2=0
        while root2:
            if l2==(l//2):
                root2.next=root2.next.next
                break
            l2+=1
            root2=root2.next
        return root.next