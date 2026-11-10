class node:
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.left = None
        self.right = None

class MyCalendar:
    def __init__(self):
      self.root = None

    def helper(self, root, s, e):
        r_s = root.s
        r_e = root.e

        if(e < r_s):
            if(root.left == None):
                root.left = node(s, e)
                return True
            return self.helper(root.left, s, e)
        if(s > r_e):
            if(root.right == None):
                root.right = node(s, e)
                return True
            return self.helper(root.right, s, e)

        return False

    def book(self, startTime: int, endTime: int) -> bool:
        if(self.root == None):
            self.root = node(startTime, endTime-1)
            return True
        return self.helper(self.root, startTime, endTime-1)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)