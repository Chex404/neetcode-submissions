# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         prev, curr = None, head

#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp

#         delete_prev = prev

#         for i in range(n-2):
#             delete_prev = delete_prev.next

#         delete = delete_prev.next
#         if delete.next:
#             delete_prev.next = delete.next
#         else:
#             delete_prev.next = None

#         prev1, curr = None, prev

#         while curr:
#             temp = curr.next
#             curr.next = prev1
#             prev1 = curr
#             curr = temp

#         return prev1
    

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reverse the list
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # prev is now the head of the reversed list
        if n == 1:
            # Removing the last node of the original list
            # = removing the head of the reversed list
            prev = prev.next
        else:
            delete_prev = prev
            for i in range(n - 2):
                delete_prev = delete_prev.next

            delete = delete_prev.next
            delete_prev.next = delete.next if delete else None

        # Reverse back
        prev1, curr = None, prev
        while curr:
            temp = curr.next
            curr.next = prev1
            prev1 = curr
            curr = temp

        return prev1