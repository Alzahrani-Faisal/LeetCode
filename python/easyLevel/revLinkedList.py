# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = head
        pointer2 = None
        while pointer1:
            temp = pointer1.next
            pointer1.next = pointer2
            pointer2 = pointer1
            pointer1 = temp
        return pointer2
