class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for e in s:
            dic[e] = dic.get(e, 0)+1
        ar = []
        for key, val in dic.items():
            ar.append([val, key])
        ar.sort(key = lambda x: x[0])

        ans = ""
        for i in range(len(ar)-1, -1, -1):
            ans+=(ar[i][1]*ar[i][0])
        return ans