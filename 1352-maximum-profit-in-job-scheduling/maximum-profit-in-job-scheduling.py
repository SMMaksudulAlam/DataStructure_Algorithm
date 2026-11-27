class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = []

        for i in range(len(startTime)):
            jobs.append((startTime[i], endTime[i], profit[i]))
        
        jobs.sort(key = lambda x:x[0])

        """
        @lru_cache(None)
        def schedule(last, current):
            if(current>=len(jobs)):
                return 0
            
            last_end = -1
            if(last>=0):
                last_end = jobs[last][1]
            
            prft = 0
            if(last_end<=jobs[current][0]):
                prft = jobs[current][2] + schedule(current, current+1)
            
            prft = max(prft, schedule(last, current+1))

            return prft
        
        ans = schedule(-1, 0)
        return ans
        """
        #it works but the complexity is O(n*n)

        # i can optimize it by using the binary search for schedule(current, current+1)

        def bin_search(current):
            left = current
            right = len(jobs)-1

            if(jobs[current][1] > jobs[right][0]):
                return right+1
            
            ans = current + 1
            while(left <= right):
                mid = (left+right) // 2
                if(jobs[mid][0] >= jobs[current][1]):
                    ans = mid
                    right = mid-1
                else:
                    left = mid+1
            return ans

        @lru_cache(None)
        def schedule(current):
            if(current>=len(jobs)):
                return 0

            next_ind = bin_search(current)
            prft = jobs[current][2] + schedule(next_ind)
            
            prft = max(prft, schedule(current+1))

            return prft
        
        ans = schedule(0)
        return ans