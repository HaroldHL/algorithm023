# def mergeTwoLists(l1: ListNode, l2: ListNode):
#         # Def a dump node / result will be the next of Dump node
#         dummy = ListNode(0)
#         # Def a cursor to move
#         cur = dummy
#         while l1 and l2:
#             if l1.val < l2.val:
#                 cur.next = l1
#                 l1 = l1.next
#             else:
#                 cur.next = l2
#                 l2 = l2.next
#             cur = cur.next
#         # if l1 or l2 has remaining value
#         cur.next = l1 if l1 else l2
#         return dummy.next