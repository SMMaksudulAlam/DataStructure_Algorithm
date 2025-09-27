class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k = 0
        while(True):
            rem = num1 - k*num2
            if(rem<k):
                return -1
            if(rem.bit_count()<=k):
                return k
            k+=1
        return -1