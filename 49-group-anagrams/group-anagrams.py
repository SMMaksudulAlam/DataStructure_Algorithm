class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            s_ = "".join(sorted(s))
            if(s_ not in dic):
                dic[s_] = []
            dic[s_].append(s)
        
        ans = []
        for v in dic.values():
            ans.append(v)
        return ans