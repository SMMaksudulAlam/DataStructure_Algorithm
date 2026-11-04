class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        two = len(nums)-1
        one = 0

        while(one<=two):
            if(nums[one] == 0):
                nums[zero], nums[one] = nums[one], nums[zero]
                if(zero == one):
                    one+=1
                zero += 1
            elif(nums[one] == 2):
                nums[two], nums[one] = nums[one], nums[two]
                two -= 1
            else:
                one+=1
        return
        