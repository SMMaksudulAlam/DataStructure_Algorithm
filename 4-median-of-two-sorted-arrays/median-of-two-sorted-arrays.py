class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)

        if(len1>len2):
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1
        
        left1, right1 = 0, len1-1

        half = (len1+len2)//2

        #print(nums1, nums2, len1, len2)
        while(True):
                ind1 = (left1+right1)//2

                num1 = nums1[ind1] if ind1>=0 else -inf
                num_r1 = nums1[ind1+1] if ind1+1<len1 else inf

                ind2 =  half - (ind1+1) - 1   
                #print(ind1, ind2)
                num2 = nums2[ind2] if ind2>=0 else -inf
                num_r2 = nums2[ind2+1] if ind2+1<len2 else inf

                if(num1<=num_r2 and num2<=num_r1):
                    #print(len1, len2, num1, num2, num_r1, num_r2)
                    if((len1+len2)%2==0):
                        return (max(num1, num2) + min(num_r1, num_r2))/2.0
                    else:
                        return min(num_r1, num_r2)
                elif(num1>num_r2):
                    right1 = ind1-1
                else:
                    left1 = ind1+1
        return -1

