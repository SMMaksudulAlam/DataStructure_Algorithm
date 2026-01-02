class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr)-1
        if(arr[-1] == len(arr)):
            return arr[-1] + k
        
        if(arr[-1]-len(arr) <k):
            return k + len(arr)
        
        if(arr[0]>k):
            return k
        
        while(left<=right):
            #print(left, right)
            if(left==right):
                if(arr[left]-left-1 == k):
                    return left+k
                return k+left+1
            if(left+1==right):
                if(arr[left]-left-1 == k):
                    return left+k
                elif(arr[left]-left-1 < k):
                    return k+left+1
                else:
                    return k+right+1
            mid = (left+right)//2
            if(arr[mid]-mid-1 >= k):
                right = mid
            else:
                left = mid
        return -1
