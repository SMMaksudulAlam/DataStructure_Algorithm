class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if(len(nums1)>len(nums2)):
            nums1, nums2 = nums2, nums1

        total_len = len(nums1)+len(nums2)
        half_len = total_len // 2

        lInd = 0
        rInd = len(nums1)-1
        #print(total_len)

        while(True):
            
            mid = (lInd+rInd)//2

            left1 = nums1[mid] if mid>=0 else -inf
            right1 = nums1[mid+1] if mid+1<len(nums1) else inf

            remaining_count = half_len - (mid+1)

            ind = remaining_count-1

            left2 = nums2[ind] if ind>=0 else -inf
            right2 = nums2[ind+1] if ind+1<len(nums2) else inf

            #print(lInd, rInd, "      ", ind, ind+1)

            if(left1<=right2 and left2<=right1):
                if(total_len%2!=0):
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2))/2

            else:
                if(left1>right2):
                    rInd = mid-1

                else:
                    lInd = mid+1

        return -1


