class RandomizedCollection:

    def __init__(self):
        self.dic = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        was_present = False

        if(val not in self.dic):
            was_present = True
            self.dic[val] = set()

        self.dic[val].add(len(self.lst))
        self.lst.append(val)

        #print(self.dic, self.lst)
        return was_present

    def remove(self, val: int) -> bool:
        if(val not in self.dic):
            return False
        
        val_ind = None
        for ind in self.dic[val]:
            val_ind = ind
            break

        last_elem = self.lst[-1]
        last_ind = len(self.lst) - 1

        if(last_elem != val):
            self.lst[val_ind], self.lst[last_ind] = self.lst[last_ind], self.lst[val_ind]
            self.dic[last_elem].remove(last_ind)
            self.dic[last_elem].add(val_ind)

            self.lst.pop()
            self.dic[val].remove(val_ind)

        else:
            self.lst.pop()
            self.dic[val].remove(last_ind)

        if(not self.dic[val]):
            del self.dic[val]

        #print("del", self.dic, self.lst)
        return True

    def getRandom(self) -> int:
        elem = random.choice(self.lst)
        return elem
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()