class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        def merge(left, right):
            nonlocal count
            temp = []
            l = len(left)
            r = len(right)
            #print(left, right)
            il = 0
            ir = 0

            while(il<l and ir<r):
                a = left[il]
                b = right[ir]
                
                if(a<=b):
                    temp.append(a)
                    il+=1
                else:
                    ind = bisect.bisect_right(left, 2*b)
                    count += (l-ind)
                    #print(f'for {b}, count increased: {l-ind}')
                    temp.append(b)
                    ir+=1

            if(il<l):
                temp+=left[il:]
            if(ir<r):
                for b in right[ir:]:
                    ind = bisect.bisect_right(left, 2*b)
                    count += (l-ind)
                    #print(f'for {b}, count increased: {l-ind}')
                    temp.append(b)

            #print(f'finally,  {temp}, {count}')
            return temp
        
        def split(lst):
            if(len(lst)==1):
                return lst
            mid = len(lst)//2

            left = lst[:mid]
            right = lst[mid:]

            left = split(left)
            right = split(right)

            merged = merge(left, right)
            return merged
        
        split(nums)
        return count


