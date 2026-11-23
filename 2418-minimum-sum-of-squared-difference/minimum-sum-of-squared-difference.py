class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        #3 3 5 5 5 -> 75 + 18 = 92
        #3 3 3 5 5 -> 50 + 27 = 77
        #3 3 4 4 5 --> 25 + 32 + 18 = 75

        diff_array = []
        for i in range(len(nums1)):
            diff_array.append(abs(nums1[i]-nums2[i]))

        dic = {}
        for e in diff_array:
            dic[e] = dic.get(e, 0) + 1
        dic[0] = dic.get(0, 0) + 0
        
        diff_count_array = []
        for k, v in dic.items():
            diff_count_array.append([k, v])

        diff_count_array.sort(key = lambda x:x[0]) #[(0, 0), (3, 1), (4, 3)]

        k = k1+k2 #2

        while(k>0):
            if(len(diff_count_array) == 1):
                break

            num, cnt = diff_count_array.pop() #4, 3
            
            diff_with_prev = num - diff_count_array[-1][0] # 1
            
            if(cnt*diff_with_prev <= k):
                diff_count_array[-1][1] += cnt
                k -= cnt*diff_with_prev 
            else:
                if(k<cnt):
                    diff_count_array.append([num-1, k]) #.. [3, 2]
                    diff_count_array.append([num, cnt-k]) #.. [3, 2] [4, 1]
                    break
                else:
                    dist_portion = k//cnt
                    diff_count_array.append([num-dist_portion, cnt])
                    k = k % cnt
        
        ans = 0
        for d, cnt in diff_count_array:
            ans += (d*d*cnt)
        
        return ans