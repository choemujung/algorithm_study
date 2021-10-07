# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = prev = ListNode(next=head)  # prev와 head가 이동하는 풀이이므로 root.next를 리턴
        pre_first = first = None
        idx = 1  # 반복문 한번 돌때마다 +1

        # idx가 right보다 작을때까지 반복
        while idx <= right:
            if left < idx <= right:
                head.next, prev, head = prev, head, head.next
            else:
                if idx == left:
                    pre_first, first = prev, head

                prev, head = head, head.next

            idx += 1
        pre_first.next, first.next = prev, head
        return root.next

