class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        res.append(0)
        ind = 0
        for i in range(1, n+1):
            temp = []
            for e in res:
                if(len(res)+len(temp)==n+1):
                    break
                temp.append(e+1)
            res+=temp
        return res
