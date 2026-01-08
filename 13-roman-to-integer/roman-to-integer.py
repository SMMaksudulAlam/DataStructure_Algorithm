class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {}
        dic['I'] = 1
        dic['V'] = 5
        dic['X'] = 10
        dic['L'] = 50
        dic['C'] = 100
        dic['D'] = 500
        dic['M'] = 1000

        dic['IV'] = 4
        dic['IX'] = 9
        dic['XL'] = 40
        dic['XC'] = 90
        dic['CD'] = 400
        dic['CM'] = 900

        ans = 0
        i = 0
        while(i<len(s)):
            d_ch = s[i:i+2]
            if(d_ch in dic):
                ans+=dic[d_ch]
                i+=2
            else:
                ans+=dic[s[i]]
                i+=1
        return ans