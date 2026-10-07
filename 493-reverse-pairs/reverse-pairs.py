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
                l_num = left[l_i]
                r_num = right[r_i]
                if(l_num > r_num*2):
                    temp_ans += (l_len - l_i)
                    r_i += 1
                else:
                    l_i += 1
            ans += temp_ans
            
            m_arr = []
            l_i = 0
            r_i = 0
            while(l_i<l_len and r_i<r_len):
                l_num = left[l_i]
                r_num = right[r_i]
                if(l_num <= r_num):
                    m_arr.append(l_num)
                    l_i+=1
                else:
                    m_arr.append(r_num)
                    r_i+=1
            if(l_i<l_len):
                m_arr += left[l_i:]
            if(r_i<r_len):
                m_arr += right[r_i:]

            return m_arr


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