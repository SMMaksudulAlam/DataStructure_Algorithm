class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def comb(ar, sm, ind):
            nonlocal target
            if(sm == target):
                ans.append(ar)
                return

            for i in range(ind, len(candidates)):
                e = candidates[i]
                if(sm+e<=target):
                    comb(ar+[e], sm+e, i)
                else:
                    break
            return 
        
        comb([], 0, 0)
        return ans

        