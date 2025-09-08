class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def isNoZero(n):
            while(n>0):
                if(n%10==0):
                    return False
                n//=10
            return True

        for i in range(n-1, 0, -1):
            if(isNoZero(i) and isNoZero(n-i)):
                return [i, n-i]
        return []