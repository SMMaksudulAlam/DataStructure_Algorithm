class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        i = 0
        while(True):
            rem = num1 - i*num2
            if(rem<i):
                return -1
            if(rem.bit_count()<=i):
                return i
            i+=1
        return -1