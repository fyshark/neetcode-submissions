class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.oldest = None
        self.latest = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        prev = self.latest.prev
        next = self.latest
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.key]