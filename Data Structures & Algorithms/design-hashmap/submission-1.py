class MyHashMap:

    def __init__(self):
        self.store = []

    def put(self, key: int, value: int) -> None:
        for i, (k, v) in enumerate(self.store):
            if k == key:
                self.store[i][1] = value
                return
        self.store.append([key, value]) 

    def get(self, key: int) -> int:
        for k, v in self.store:
            if key == k:
                return v
        return -1

    def remove(self, key: int) -> None:
        for k, v in self.store:
            if key == k:
                self.store.remove([key, v])


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)