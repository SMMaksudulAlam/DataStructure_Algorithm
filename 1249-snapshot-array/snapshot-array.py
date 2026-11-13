class SnapshotArray:
    """
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
    """
    #the prvious version is good, but get is worse TC. snap_id: index --> val
    #if we change the data orientation, index: snap_id --> val, it will perform better
    #why there will be no memeory issue for following one? set() inside a is increasing memory. set() will be called atmost 5*10^4 times in total, so, the worst memory will required 5*10^4.

    def __init__(self, length: int):
        self.ind = {}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if(index not in self.ind):
            self.ind[index] = []
        array = self.ind[index]
        if(not array):
            array.append([self.snap_id, val])
        else:
            if(array[-1][0] == self.snap_id):
                array[-1][1] = val
            else:
                array.append([self.snap_id, val])
        return
        #TC --> O(1)

    def snap(self) -> int:
        id = self.snap_id
        self.snap_id += 1
        return id
        #TC --> O(1)

    def get(self, index: int, snap_id: int) -> int:
        if(index not in self.ind):
            return 0

        array = self.ind[index]

        if(snap_id < array[0][0]):
            return 0
        
        if(snap_id >= array[-1][0]):
            return array[-1][1]
        
        left = 0
        right = len(array)-1
        ans = 0
        while(left<=right):
            mid = (left+right)//2
            if(array[mid][0] <= snap_id):  #i missed here. mid is the index, we need to compare the content on the index, but i directly used the index as mid <= snap_id
                ans = array[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return ans
        #TC --> O(snap)



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)