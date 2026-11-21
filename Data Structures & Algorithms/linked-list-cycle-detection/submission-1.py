# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        res = {}
        curr = head
        while curr:
            res[curr] = res.get(curr, 0) + 1
            if res.get(curr) > 1:
                return True
            curr = curr.next

        return False