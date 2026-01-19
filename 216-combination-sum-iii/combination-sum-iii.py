import heapq as hq
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        temp = [[0]]
        ans = []
        for num in nums:
            temp_ = []
            for ar in temp:
                temp_.append(ar)
                sm = ar[-1]
                if(sm+num ==n):
                    if(len(ar)==k):
                        ar_ = ar[:]
                        ar_[-1] = num
                        ans.append(ar_)
                if(sm+num <n):
                    if(len(ar)<k):
                        ar_ = ar[:]
                        ar_[-1] = num
                        ar_.append(sm+num)
                        temp_.append(ar_)
            temp = temp_
        return ans



