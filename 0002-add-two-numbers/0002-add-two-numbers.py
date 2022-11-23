# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def plus(lst,root1,root2,left=0):
            if not root1 and not root2:
                if left:
                    lst.next=ListNode(left)
                return lst
            elif root1 and root2:
                added=root1.val+root2.val+left
                lst.next=ListNode(added%10)
                return plus(lst.next,root1.next,root2.next,added//10)
            elif root1:
                app=root1.val+left
                lst.next=ListNode(app%10)
                return plus(lst.next,root1.next,root2,app//10)
            elif root2:
                app=root2.val+left
                lst.next=ListNode(app%10)
                return plus(lst.next,root1,root2.next,app//10)
        ans=ListNode(0)
        do=plus(ans,l1,l2)
        return ans.next
            