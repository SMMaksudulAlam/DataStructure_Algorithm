class Solution:
    def minDistance(self, houses: list[int], k: int) -> int:
        """
        houses.sort()

        def count_groups(dis):
            count = 0
            left = -math.inf
            for i in range(len(houses)):
                val = houses[i]
                if(left + dis >= val):
                    continue
                else:
                    count += 1
                    left = houses[i]
            return count

        left = 0
        right = houses[-1] - houses[0]

        dis = math.inf
        while(left<=right):
            mid = (left + right) // 2
            k_ = count_groups(mid)
            if(k_<=k):
                dis = mid
                right = mid - 1
            else:
                left = mid + 1
        
        
        arr = []
        left = -math.inf
        for i in range(len(houses)):
            val = houses[i]
            if(left + dis >= val):
                arr[-1][1] = i
            else:
                arr.append([i, i])
                left = houses[i]

        if(len(arr)<k):
            distances = []
            for i, j in arr:
                median = houses[(i+j)//2]
                for ind in range(i, j+1):
                    distances.append(abs(houses[ind] - median))

            distances.sort()
            carry_k = k - len(arr)
            eleminated_distanes = {}
            while(carry_k>0):
                d = distances.pop()
                eleminated_distanes[d] = eleminated_distanes.get(d, 0) + 1
                carry_k -= 1

            #adjust the even-counted groups
            for arr_ind, (i, j) in enumerate(arr):
                median = houses[(i+j)//2]
                for ind in range(i, j+1):
                    d = abs(houses[ind] - median)
                    if(d in eleminated_distanes and (j-i+1)%2 == 0):
                        if(ind == i):
                            arr[arr_ind][0] += 1
                        elif(ind == j):
                            arr[arr_ind][1] -= 1
                        eleminated_distanes[d]-=1
                        if(eleminated_distanes[d] == 0):
                            del eleminated_distanes[d]
        
        ans = 0
        distances = []
        for i, j in arr:
            median = houses[(i+j)//2]
            for ind in range(i, j+1):
                ans += abs(houses[ind] - median)

        return ans
        """
        # i tried my best in the following ways:
        # binary search to find optimal max-distance of group-elements, while keeping the group-count is at most k
        # it works if we get k group-count, but, if we get <k group-count, there is a problem, now we can slit the groups
        # but which one? i tried to do it shrinking the group holding highest distance from left or right most element by increasing or decresing the edge-indices in a range.
        # but, here is another problem, what if the same group needs to be splited in other way?
        # Damn, i can't handle more! So, i quit the approach.


        houses.sort()
        length = len(houses)
        dis_in_ranges = []
        for i in range(length):
            dis_in_ranges.append([math.inf]*length)
        
        for i in range(length):
            for j in range(i, length):
                median = houses[(i+j)//2]
                dis = 0
                for ind in range(i, j+1):
                    dis += abs(houses[ind]-median)
                dis_in_ranges[i][j] = dis

        @lru_cache(None)
        def pick_ranges(ind, grp):
            if(ind == length):
                return 0
            if(grp > k):
                return math.inf
            
            ans = math.inf
            for i in range(ind, length):
                ans = min(ans, dis_in_ranges[ind][i] + pick_ranges(i+1, grp+1))

            return ans
        
        ans = pick_ranges(0, 1)
        return ans
            


