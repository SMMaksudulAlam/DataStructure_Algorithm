class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            d = int(num[i])
            if(d%2==1):
                return num[:i+1]
        return ""