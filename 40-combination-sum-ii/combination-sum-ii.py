class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        #i misunderstood the problem and the following implementation was to generate all unique possible collection with repeating elements that sums to target
        nums = set(candidates)
        nums = list(nums)
        #print(nums)

        def comb_sum(target, ind):
            if(target == 0):
                return [[nums[ind]]]
            if(ind<0):
                return []
            
            ans = []
            if(target >= nums[ind]):
                ans_ = comb_sum(target - nums[ind], ind)
                num = nums[ind]
                for e in ans_:
                    e.append(num)
                    ans.append(e)

            ans += comb_sum(target, ind-1)

            return ans
        
        ans = comb_sum(target, len(nums)-1)
        return ans
        """

        nums = candidates
        nums.sort()
        
        def comb_sum(target, ind):
            if(target == 0):
                return set()
            if(ind<0):
                return set()
            
            ans = []
            if(target >= nums[ind]):
                ans_ = comb_sum(target - nums[ind], ind-1)
                num = nums[ind]
                for e in ans_:
                    e.append(num)
                    ans.append(e)
                if(not ans_ and target == num):
                    ans.append([num])
            
            i = ind-1
            while(i>=0 and nums[i]==nums[i+1]):
                i-=1
                continue
            ans_ = comb_sum(target, i)
            ans += ans_
            return ans
    
        ans = comb_sum(target, len(nums)-1)
        return list(ans)