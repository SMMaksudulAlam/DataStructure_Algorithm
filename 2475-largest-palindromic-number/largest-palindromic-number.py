import heapq as hq
class Solution:
    def largestPalindromic(self, num: str) -> str:
        #print(len(num))
        freq = {}
        for n in num:
            freq[n] = freq.get(n, 0)+1
        
        h = []
        sngl = []

        for k, val in freq.items():
            k = int(k)
            hq.heappush(h, (-k, val//2))
            if(val%2!=0):
                sngl.append(k)
        
        sngl.sort()
        #print(h, sngl)
        ans = ""
        track = None
        while(h):
            k, val = hq.heappop(h)
            k = -k
            if(not ans and k==0):
                continue
            ans+= str(k)*val
        
        if(sngl):
            ans = ans + str(sngl[-1]) + ans[::-1]
        else:
            ans = ans + ans[::-1]

        return ans if ans else "0"