# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# first approach--
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         arr = []

#         curr = head
#         while curr:
#             arr.append(curr)
#             curr = curr.next

#         return arr[len(arr) // 2]  



# implemented solution--
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         slow = head
#         fast = head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         return slow