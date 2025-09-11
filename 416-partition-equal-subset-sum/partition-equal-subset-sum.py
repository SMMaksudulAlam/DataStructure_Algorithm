class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if(s%2!=0):
            return False
        
        ss = s//2
        
        s = set()
        s.add(0)

        for n in nums:
            s_ = set()
            for n_ in s:
                s_.add(n_+n)
                s_.add(n_)
                if(n_+n==ss):
                    return True
            s = s_
        return False


        