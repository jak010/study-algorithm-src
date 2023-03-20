# 206, Reverse Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# def reverseList(head: ListNode) -> ListNode:
#     def reverse(node: ListNode, prev: ListNode = None):
#         if not node:
#             return prev
#         nxt, node.next = node.next, prev
#         return reverse(nxt, node)
#
#     return reverse(head)


def reverseList(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = None

    head = l1

    # while head:
    #     print(head.val)
    #     head = head.next
    #
    z = reverseList(head)

    while z:
        print(z.val)
        z = z.next

    # while head:
    #     print(head.val)
    #     head = head.next
