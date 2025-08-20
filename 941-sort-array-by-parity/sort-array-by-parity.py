class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        eInd = 0
        oInd = 0
        while(oInd<len(nums) and eInd<len(nums)):
            noO = True
            while(oInd<len(nums)):
                if(nums[oInd]%2==1):
                    noO = False
                    break
                oInd += 1
            if(noO == False):
                noE = True
                eInd = oInd + 1
                while(eInd<len(nums)):
                    if(nums[eInd]%2==0):
                        noE = False
                        break
                    eInd += 1

                if(noE == False):
                    nums[oInd], nums[eInd] = nums[eInd], nums[oInd]
                    oInd += 1

            #print(nums, oInd, eInd)
        return nums

