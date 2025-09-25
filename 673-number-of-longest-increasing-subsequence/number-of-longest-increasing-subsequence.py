class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        ar = []
        LEN = 1
        for e in nums:
            temp = []
            mx_len = 1
            count = 1
            while(ar):
                val, ln, cnt = ar.pop()
                temp.append((val, ln, cnt))
                if(val<e):
                    if(ln+1==mx_len):
                        count+=cnt
                    elif(ln+1>mx_len):
                        mx_len = ln+1
                        count = cnt
                    else:
                        pass
            for pre in temp:
                ar.append(pre)
            ar.append((e, mx_len, count))
            LEN = max(LEN, mx_len)
        count = 0
        for e, ln, cnt in ar:
            if(ln==LEN):
                count+=cnt
        return count
                    

        



            