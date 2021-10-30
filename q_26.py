class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MyCircularDeque:


    def __init__(self, k: int):
        self.head = self.tail = ListNode()
        self.k, self.len = k, 0
    def insertFront(self, value: int) -> bool:
        if self.k == self.len:
            return False
        if self.len == 0:
            self.head.val = value
        else:
            self.head.left = ListNode(val=value, right=self.head)
            self.head = self.head.left
        self.len += 1
        return True
    def insertLast(self, value: int) -> bool:
        if self.k == self.len:
            return False
        if self.len == 0:
            self.tail.val = value
        else:
            self.tail.right = ListNode(val=value, left=self.tail)
            self.tail = self.tail.right
        self.len += 1
        return True
    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.head, self.head.right = self.head.right, None
        self.head.left = None
        self.len -= 1
        return True
    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.tail, self.tail.left = self.tail.left, None
        self.tail.right = None
        self.len -= 1
        return True
    def getFront(self) -> int:
        if self.len == 0:
            return -1
        return self.head.val
    def getRear(self) -> int:
        if self.len == 0:
            return -1
        return self.tail.val
    def isEmpty(self) -> bool:
        if self.len == 0:
            return True
        else:
            return False
    def isFull(self) -> bool:
        if self.len == self.k:
            return True
        else:
            return False
