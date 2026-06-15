class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)

        if(len1>len2):
            len1, len2 = len2, len1
            nums1, nums2 = nums2, nums1
        
        total_count = len1+len2
        left_part_count = (total_count // 2)

        left1 = 0
        right1 = len1 - 1

        while(True):
            mid1 = (left1 + right1) // 2
            mid_e11 = nums1[mid1] if(nums1 and mid1>=0) else -inf
            mid_e12 = nums1[mid1+1] if(nums1 and mid1+1<len1) else inf

            rest = left_part_count - (mid1 + 1)
            mid2 = rest - 1
            mid_e21 = nums2[mid2] if(nums2 and mid2>=0) else -inf
            mid_e22 = nums2[mid2+1] if(nums2 and mid2+1<len2) else inf

            if(mid_e11 <= mid_e22 and mid_e21 <= mid_e12):
                #print(mid_e11, mid_e12, ">>>", mid_e21, mid_e22)
                if(total_count%2==1):
                    return min(mid_e12, mid_e22)
                else:
                    return (min(mid_e12, mid_e22) + max(mid_e11, mid_e21))/2
            
            if(mid_e11 > mid_e22):
                right1 = mid1-1
            else:
                left1 = mid1+1

        return -1