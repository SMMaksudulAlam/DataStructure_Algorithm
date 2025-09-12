class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while(l<r):
            e1 = numbers[l]
            e2 = numbers[r]

            s = e1+e2
            if(s==target):
                return [l+1, r+1]
            if(s<target):
                l+=1
            else:
                r-=1
        return []
            