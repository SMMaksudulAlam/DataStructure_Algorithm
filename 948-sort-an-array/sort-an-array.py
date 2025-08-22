class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def margeSort(lst):
            if(len(lst)<=1):
                return lst

            mid = len(lst)//2
            lft = margeSort(lst[:mid])
            rght = margeSort(lst[mid:])

            ans = []
            l = 0
            r = 0

            while(l<len(lft) and r<len(rght)):
                if(lft[l]<=rght[r]):
                    ans.append(lft[l])
                    l+=1
                else:
                    ans.append(rght[r])
                    r+=1
            
            if(l<len(lft)):
                ans+=lft[l:]
            if(r<len(rght)):
                ans+=rght[r:]
                
            return ans

        nums = margeSort(nums)
        return nums