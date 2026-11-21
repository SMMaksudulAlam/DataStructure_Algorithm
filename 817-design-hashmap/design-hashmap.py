class MyHashMap:

    def __init__(self):
        limit = 10**6
        self.arr = [-1]*(limit+1)

    def put(self, key: int, value: int) -> None:
        self.arr[key] = value
        return

    def get(self, key: int) -> int:
        return self.arr[key]

    def remove(self, key: int) -> None:
        self.arr[key] = -1
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)