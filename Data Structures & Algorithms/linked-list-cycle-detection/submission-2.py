# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        node = head

        while node != None:
            if node not in visited:
                visited.add(node)
            
            else:
                return True
            node = node.next

        return False




            


        