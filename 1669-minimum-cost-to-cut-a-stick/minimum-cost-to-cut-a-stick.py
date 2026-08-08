class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """  
        #The greedy solution on heuristic: cut at closest to mid point will give optimal cost

        cuts.sort()
        #print(cuts)

        def cut_ind(point):
            if(point<=cuts[0]):
                return cuts[0]
            if(point>=cuts[-1]):
                return cuts[-1]
            
            left = 0
            right = len(cuts)-1

            while(True):
                if(left+1 == right):
                    if(point-cuts[left]) <= (cuts[left+1]-point):
                        return cuts[left]
                    return cuts[right]
                
                mid = (left+right)//2
                if(cuts[mid] > point):
                    right = mid
                else:
                    left = mid
            return -1

        
        #print(cut_ind(2), cut_ind(3), cut_ind(-1), cut_ind(10))

        def cut_stick(left_ind, right_ind):
            mid_ind = (left_ind+right_ind)//2
            optimal_ind = cut_ind(mid_ind)
            if(optimal_ind<=left_ind or optimal_ind>=right_ind):
                return 0
            
            left_cuts = cut_stick(left_ind, optimal_ind)
            right_cuts = cut_stick(optimal_ind, right_ind)
            ans = (right_ind - left_ind) + left_cuts + right_cuts
            return ans

        ans = cut_stick(0, n)
        return ans
        """

        cuts.sort()
        #print(cuts)

        def cut_ind(left_ind):
            if(left_ind<=cuts[0]):
                return 0
            if(left_ind>cuts[-1]):
                return -1

            left = 0
            right = len(cuts)-1

            while(True):
                if(left+1 == right):
                    if(cuts[left] >= left_ind):
                        return left
                    return right
                
                mid = (left+right)//2
                if(cuts[mid] >= left_ind):
                    right = mid
                else:
                    left = mid
            return -1

        dp = {}
        def cut_stick(left_ind, right_ind):
            if((left_ind, right_ind) in dp):
                return dp[(left_ind, right_ind)]
            ind = cut_ind(left_ind+1)
            if(ind == -1 or cuts[ind]>=right_ind):
                return 0
            i = ind
            ans = inf
            while(i<len(cuts) and cuts[i]<right_ind):
                left_cuts = cut_stick(left_ind, cuts[i])
                right_cuts = cut_stick(cuts[i], right_ind)
                temp_ans = (right_ind - left_ind) + left_cuts + right_cuts
                ans = min(ans, temp_ans)
                i+=1
            
            #print("left, right, ans", left_ind, right_ind, ans)
            dp[(left_ind, right_ind)] = ans
            return ans
        
        ans = cut_stick(0, n)
        return ans
            
