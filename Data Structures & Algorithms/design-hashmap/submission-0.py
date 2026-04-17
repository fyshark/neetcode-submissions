class MyHashMap:

    def __init__(self):
        self.mp = []

    def put(self, key: int, value: int) -> None:
        for i, (k, v) in enumerate(self.mp):
            if key == k:
                self.mp[i] = [key, value]
                return
        self.mp.append((key, value))    

    def get(self, key: int) -> int:
        for k, v in self.mp:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for i, (k, v) in enumerate(self.mp):
            if k == key:
                self.mp.pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)