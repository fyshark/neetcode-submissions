class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.capacity = k
        self.head, self.tail = Node(0), Node(0)
        self.head.next, self.tail.prev = self.tail, self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        node = Node(value)
        prev = self.tail.prev

        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node
        self.capacity -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        node_to_be_removed = self.head.next
        prev, nxt = node_to_be_removed.prev, node_to_be_removed.next
        prev.next, nxt.prev = nxt, prev
        self.capacity += 1
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.head.next.value
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.tail.prev.value
        return -1

    def isEmpty(self) -> bool:
        if self.capacity == self.k:
            return True
        return False

    def isFull(self) -> bool:
        if not self.capacity:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()