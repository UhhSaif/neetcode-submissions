# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # shift right to intial pos
        while n > 0 and right:
            right = right.next
            n -= 1

        # get left to pos
        while right:
            left = left.next
            right = right.next

        # delete nth node
        left.next = left.next.next
        return dummy.next

            