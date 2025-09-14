class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        dic = {}
        ans = []
        candidates.sort()
        def build(temp, sum, ind):
            nonlocal target
            if(sum==target):
                s = "".join([str(e) for e in temp])
                if(s not in dic):
                    ans.append(temp)
                    dic[s] = 1
                return
            if(sum>target):
                return
            
            for i in range(ind, len(candidates)):
                if(i>ind and candidates[i]==candidates[i-1]):
                    continue
                e = candidates[i]
                build(temp+[e], sum+e, i+1)
            
            return
        
        build([], 0, 0)
        return ans