class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        """
        def build(ind, target): #6, 5
            if(target == 0):
                return True, set()
            if(ind<0):
                return False, set()
            
            if(target>=nums[ind]):
                t_f, ind_ar = build(ind-1, target-nums[ind]) #3, 2
                if(t_f):
                    ind_ar.add(ind)
                    return True, ind_ar
            
            t_f, ind_ar = build(ind-1, target)
            if(t_f):
                return True, ind_ar
            return False, set()
        
        sm = sum(nums)

        if(sm%k != 0):
            return False

        nums.sort()
        target = sm // k  #5
        print("nums", nums, "target", target)
        for i in range(k):
            t_f, ind_ar = build(len(nums)-1, target) #6, 5
            if(not t_f):
                return False
            nums_ = []
            print(ind_ar)
            for i in range(len(nums)):
                if(i in ind_ar):
                    continue
                nums_.append(nums[i])
            nums = nums_
            print(nums)
        return True

        #it was close, 162/164 testcases passed
        """

        sm = sum(nums)
        if(sm%k != 0):
            return False
        target = sm // k
        used = [False]*len(nums)
        dp = {}

        def partition(sm, count):
            key = ""
            for e in used:
                key += str(e) 
            key += " "+str(sm)+" "+str(count)
            if(key in dp):
                return dp[key] #i returned dp only
            

            if(sm == target):
                if(count == k and all(used)):
                    return True
                else:
                    return partition(0, count+1)
            if(all(used)):
                return False
            
            for i in range(len(nums)):
                if(used[i] == False):
                    used[i] = True
                    if(sm + nums[i] <= target):
                        if(partition(sm + nums[i], count)):
                            return True
                    used[i] = False

            dp[key] = False
            return False

        return partition(0, 1)