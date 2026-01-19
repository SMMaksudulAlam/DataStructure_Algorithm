class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        dic = {}
        def comb(ar, sm, ind):
            nonlocal target
            if(sm == target):
                s = ""
                for e in ar:
                    s+=str(e)
                if(s not in dic):
                    ans.append(ar)
                    dic[s] = 1
                return

            for i in range(ind, len(candidates)):
                e = candidates[i]
                if(i>ind and  candidates[i-1] == candidates[i]):
                    continue
                if(sm+e<=target):
                    comb(ar+[e], sm+e, i+1)
                else:
                    break
            return 
        
        comb([], 0, 0)
        return ans