class Solution:
    def maximumEvenSplit(self, finalSum: int) -> list[int]:
        if(finalSum%2 == 1):
            return []

        if(finalSum <= 4):
            return [finalSum]

        ans = []
        i = 2

        while(finalSum > 2*i):
            ans.append(i)
            finalSum -= i
            i += 2

        
        if(finalSum == 2*i):
            ans.append(i)
            ans.append(i+2)
            ans = ans[1:]
        else:
            ans.append(finalSum) #i accidentally appended i here instead of finalSum

        return ans
        #TC --> O(n)