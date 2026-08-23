class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)] #[1, 2, 3, 4]
        block_size = 1
        for i in range(1, n):
            block_size *= i #6

        ans = ""
        while(nums):
            ind = (k-1)//block_size #1 1 0 0 #(k-1) is very important here.
            num = nums[ind] #2 3 1 4
            ans += num #2314

            k -=  (ind)*block_size #3 1 1 1
            block_size = block_size//(len(nums)-1) if (len(nums)-1 > 0) else 1 #2 1 1 1
            nums.remove(num) #[1, 3, 4] [1, 4] [4] []
        return ans