class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2 = None, None
        count1, count2 = 0, 0

        for n in nums:
            if(count1 == 0 and n!=num2):
                count1 += 1
                num1 = n
                continue
            
            if (count2 == 0 and n!=num1):
                count2 += 1
                num2 = n
                continue
            
            if(n == num1):
                count1+=1
            elif(n == num2):
                count2+=1
            else:
                count1-=1
                count2-=1
        
        res = []
        threshold = len(nums)//3

        if(nums.count(num1)>threshold):
            res.append(num1)
        if(nums.count(num2)>threshold):
            res.append(num2)
        return res