class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        def merge(left, right): #[[1, 8, 18, 24], [3, 7, 10]
            nonlocal ans
            l_len = len(left)
            r_len = len(right)

            l_i = 0
            r_i = 0
            temp_ans = 0

            while(l_i<l_len and r_i<r_len):
                l_e = left[l_i]
                r_e = right[r_i]
                if(l_e <= 2*r_e):
                    temp_ans += r_i #3
                    l_i += 1
                else:
                    while(r_i<r_len and l_e > 2*right[r_i]):
                        r_i += 1
            if(l_i<l_len):
                temp_ans += ((l_len-l_i)*r_len) #6
            
            ans += temp_ans
            ar = [] #[1, 8, 18, 24], [3, 7, 10]
            l_i = 0
            r_i = 0
            while(l_i<l_len or r_i<r_len): 
                l_e = left[l_i] if l_i<l_len  else inf
                r_e = right[r_i] if r_i<r_len else inf

                if(l_e <= r_e):
                    ar.append(l_e)
                    l_i += 1
                else:
                    ar.append(r_e)
                    r_i += 1
            return ar

        #ar = merge([1, 8, 18, 24], [3, 7, 10])
        #print(ans, ar)

        def m_sort(lst):
            if(len(lst)==1):
                return lst
            mid = len(lst)//2
            left = lst[:mid]
            right = lst[mid:]

            left = m_sort(left)
            right = m_sort(right)

            lst = merge(left, right)
            return lst

        nums = m_sort(nums)
        return ans 