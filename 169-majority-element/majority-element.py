class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = None

        for n in nums:
            if(count==0):
                element = n
                count+=1
            elif(n == element):
                count+=1
            else:
                count-=1
        
        if(nums.count(element)>len(nums)//2):
            return element
        return -1