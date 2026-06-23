class TimeMap:
    def __init__(self):
        self.dic = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.dic):
            self.dic[key] = []
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.dic.get(key, [])

        if(not lst or lst[0][0]>timestamp):
            return ""
        
        if(lst[-1][0]<=timestamp):
            return lst[-1][1]

        left = 0
        right = len(lst)-1

        while(left<=right):
            if(left == right):
                if(lst[right][0]<=timestamp):
                    return lst[right][1]
                else:
                    return ""
            if(left+1 == right):
                if(lst[right][0]<=timestamp):
                    return lst[right][1]
                elif(lst[left][0]<=timestamp):
                    return lst[left][1]
                else:
                    return ""
            
            mid = (left+right)//2
            if(lst[mid][0]>=timestamp):
                right = mid
            else:
                left = mid

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)