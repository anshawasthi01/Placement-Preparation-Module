# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l = l[::-1]
        a = ListNode(0)
        temp = a
        for i in l:
            temp.next = ListNode(i)
            temp = temp.next
        return a.next     
