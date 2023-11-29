# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l = []
        k = 0
        while head:
            if head not in l:
                l.append(head)
            else:
               return True
            head = head.next
        return False