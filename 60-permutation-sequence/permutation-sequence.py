class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)]
        facto = 1
        for i in range(1, n):
            facto*=i # 6
        
        ans = ""
        last = n-1
        while(facto>1):
            ind = (k-1)//facto
            #print(nums, k, facto, last, ind)
            num = nums[ind]
            ans += str(num) 
            nums.remove(num)
            k -= (ind)*facto 
            facto = facto//last if last else 1
            last -= 1 if last > 0 else 1

        #print(facto, k, nums, ans)
        if(k<=1):
            ans += ''.join(nums)
        else:
            ans += ''.join(nums[::-1])
        return ans


