class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []
        ln = len(nums)

        for i in range(len(nums)):
            if(i>0 and nums[i-1]==nums[i]):
                continue
            
            dic = {}
            target = 0-nums[i]


            l = i+1
            r = ln-1

            while(l<r):
                e1 = nums[l]
                e2 = nums[r]

                s = e1+e2

                if(s==target):
                    if((e1, e2) not in dic):
                        ans.append([nums[i], e1, e2])
                        dic[(e1, e2)] = 1
                    l+=1
                    
                elif(s<target):
                    l+=1
                else:
                    r-=1
        return ans