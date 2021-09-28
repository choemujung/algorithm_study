class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:  # head가 none이면 그대로 출력
            return head

        result = head  
        l, r = head, head.next  # 입력받은 연결리스트의 첫번째, 두번째 노드를 각각 l, r로 참조

        while l and r:  # 하나라도 none이면 종료
            l.next, r.next = r.next, l  # l, r의 next를 서로 바꿈

            if r.next.next and l.next.next:  # 앞에 노드가 두개 이상 존재하면 이동
                l, r = r.next.next, l.next.next
            else:
                break

        return result
    #실패
