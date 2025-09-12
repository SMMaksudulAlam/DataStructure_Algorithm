class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.dic):
            self.dic[key] = []
        
        self.dic[key].append((timestamp, value))
    
    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.dic):
            return ""
        
        lst = self.dic[key]
        l = 0
        r = len(lst)-1

        while(l<=r):
            if(l==r):
                if(lst[l][0]<=timestamp):
                    return lst[l][1]
                return ""
            if(l+1==r):
                if(lst[r][0]<=timestamp):
                    return lst[r][1]
                if(lst[l][0]<=timestamp):
                    return lst[l][1]
                return ""
            
            m = (l+r)//2
            if(lst[m][0]<=timestamp):
                l = m
            else:
                r = m
        return ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)