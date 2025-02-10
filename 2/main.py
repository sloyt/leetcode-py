from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head: ListNode = None
        tail: ListNode = None
        has_carry: bool = False

        while l1 or l2:
            sum_val = ((l1.val if l1 else 0) +
                       (l2.val if l2 else 0) +
                       (1 if has_carry else 0))

            sum_write = sum_val % 10
            has_carry = (sum_val - sum_write) > 0

            node = ListNode(sum_write)

            if head:
                tail.next = node
            else:
                head = node

            tail = node

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if has_carry:
            tail.next = ListNode(1)

        return head


s = Solution()


def fill(arr: list[int]) -> ListNode:
    head: ListNode = ListNode(arr[0])
    tail: ListNode = head

    for i in range(1, len(arr)):
        tail.next = ListNode(arr[i])
        tail = tail.next

    return head


def print_list(l: ListNode):
    while l is not None:
        print(l.val, end=' ')
        l = l.next


print(print_list(s.addTwoNumbers(fill([2, 4, 3]), fill([5, 6, 4]))))
print(print_list(s.addTwoNumbers(fill([0]), fill([0]))))
print(print_list(s.addTwoNumbers(fill([9, 9, 9, 9, 9, 9, 9]), fill([9, 9, 9, 9]))))
print(print_list(s.addTwoNumbers(fill([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), fill([5, 6, 4]))))
