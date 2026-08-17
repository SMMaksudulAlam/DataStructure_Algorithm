class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        ind1 = m-1
        ind2 = n-1
        ind = (m+n)-1

        for i in range(ind, -1, -1):
            num1 = nums1[ind1] if ind1>=0 else -inf
            num2 = nums2[ind2] if ind2>=0 else -inf
            
            if(num1>=num2):
                nums1[i] = num1
                ind1-=1
            else:
                nums1[i] = num2
                ind2-=1