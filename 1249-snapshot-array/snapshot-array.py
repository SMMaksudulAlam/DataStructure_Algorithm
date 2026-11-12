class SnapshotArray:

    def __init__(self, length: int):
        self.track = {}
        self.temp = {}

    def set(self, index: int, val: int) -> None:
        self.temp[index] = val
        return
        #TC --> O(1)

    def snap(self) -> int:
        id = len(self.track.keys())
        self.track[id] = self.temp
        self.temp = {}
        return id
        #TC --> O(1)

    def get(self, index: int, snap_id: int) -> int:
        id = snap_id
        while(id>=0):
            if(index in self.track[id]):
                return self.track[id][index]
            id-=1
        return 0
        #TC --> O(snap)


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)