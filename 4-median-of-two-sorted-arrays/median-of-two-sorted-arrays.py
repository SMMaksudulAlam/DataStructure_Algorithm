class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2
        k = (len(a) + len(b) +1)//2
            
        if(len(a)>len(b)):
            a, b = b, a
        
        len_a = len(a)
        len_b = len(b)
        
        left = -1
        right = len_a
        
        while(left<=right):
            mid = (left+right)//2
            left_a = a[mid] if mid>=0 else -math.inf
            right_a = a[mid+1] if mid+1 < len_a else math.inf
            
            rest = k-(mid+1)
            
            b_ind = rest-1
            left_b = None
            if(0<=b_ind<len_b):
                left_b = b[b_ind]
            elif(b_ind>=len_b):
                left_b = math.inf
            else:
                left_b = -math.inf
            
            right_b = None
            if(0<=b_ind+1<len_b):
                right_b = b[b_ind+1]
            elif(b_ind+1>=len_b):
                right_b = math.inf
            else:
                right_b = -math.inf
            
            if(left_a<=right_b and left_b<=right_a):
                #print(left_a, right_a, left_b, right_b)
                if((len(a) + len(b))%2==1):
                    return max(left_a, left_b)
                else: 
                    return (max(left_a, left_b) + min(right_a, right_b))/2.0

            if(left_a>right_b):
                right = mid-1
            else:
                left = mid+1
        
        return -1