# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # In: Two LL, sorted
        # Out: One LL, sorted
        # E:
        # - Empty LL --> return the LL that exists, or if both empty, return Null
        # - If two linked lists are identical, do we care about the order of which node gets added?

        # Plan:
        # - Two pointers, 
        # - Loop to add nodes from LL1 to LL2.
        # - Iteration --> one node being added or skipped

        head = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        node.next = list1 or list2

        return head.next