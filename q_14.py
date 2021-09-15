from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 초기 노드 세팅
        tail = l1  # 결과 리스트 끝부분
        head = l1  # 결과 리스트 첫부분
        if l1.val > l2.val:  # 첫번째 노드 비교, 같으면 l1 노드 선택
            head = l2
            tail = l2
            l2 = l2.next  # 결과 리스트에 포함된 노드는 더이상 비교하지 않는다
        else:
            l1 = l1.next

        while l1 is None or l1 is None:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next

        if l1 is None:
            tail.next = l2
        elif l2 is None:
            tail.next = l1

        return head




