class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        def perm(nums):
            if(len(nums)==1):
                return [[nums[0]]]
            len_ = len(nums)
            i = 0
            ans = []
            while(i<len_):
                num = nums[0]
                rest = nums[1:]
                ans_ = perm(rest)
                for e in ans_:
                    #ans.append([num]+e)
                    e.append(num)
                    ans.append(e)
                nums = rest + [num]
                i+=1
            return ans
        
        ans  = perm(nums)
        return ans
        """

        #trying naive backtracking, all possible arrangements.

        used = [False]*len(nums)

        def perm():
            if(all(used)):
                return [[]]
            
            ans = []
            for i in range(len(nums)):
                if(not used[i]):
                    used[i] = True
                    n = nums[i]
                    ans_= perm()
                    for e in ans_:
                        e.append(n)
                        ans.append(e)
                    used[i] = False
            return ans

        return perm()

