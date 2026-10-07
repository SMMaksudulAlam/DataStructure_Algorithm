class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dic = {}
        def part(ind):
            if(ind in dic):
                return dic[ind]
            if(len(arr)-ind<=k):
                return max(arr[ind:])*(len(arr)-ind)
            ans = arr[ind]
            count = 1
            for i in range(ind, min(ind+k, len(arr))):
                ans = max(ans, max(arr[ind:i+1])*count + part(i+1))
                count+=1
            dic[ind] = ans
            return ans

        ans = part(0)
        return ans
