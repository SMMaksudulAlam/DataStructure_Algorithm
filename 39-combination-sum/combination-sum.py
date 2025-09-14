class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def build(temp, sum, ind):
            nonlocal target
            if(sum==target):
                ans.append(temp)
                return
            if(sum>target):
                return
            
            for i in range(ind, len(candidates)):
                e = candidates[i]
                build(temp+[e], sum+e, i)
            
            return
        
        build([], 0, 0)
        return ans