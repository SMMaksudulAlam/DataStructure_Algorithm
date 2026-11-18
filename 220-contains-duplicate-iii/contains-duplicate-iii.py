from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        lst = SortedList()
        for i in range(min(indexDiff+1, len(nums))): #i missed it at first, as indexDiff can be equal to len(nums)
            lst.add(nums[i])
        
        left = 0
        right = indexDiff+1

        while(right<len(nums)):
            left_elem = nums[left]
            ind = lst.bisect_left(left_elem)

            if(ind>0):
                if(left_elem - lst[ind-1] <= valueDiff):
                    return True
            if(ind+1<len(lst)):
                if(lst[ind+1] - left_elem <= valueDiff):
                    return True
            
            lst.remove(left_elem)
            left+=1
            
            lst.add(nums[right])
            right += 1
        
        while(len(lst)>1):
            if(lst[1]-lst[0] <= valueDiff):
                return True
            e = lst[0]
            lst.remove(e)
        
        return False

    #TC --> O(nlogn)