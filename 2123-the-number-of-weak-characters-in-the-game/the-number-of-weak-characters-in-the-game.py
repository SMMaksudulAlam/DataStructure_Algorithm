class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
        properties.sort(key = lambda x:x[0])
        ans = 0
        q = deque() 
        q.append(properties[-1][1])

        for i in range(len(properties)-2, -1, -1):
            maxi = max(q[0], properties[i][1])
            q.appendleft(maxi)
        
        def bisect_right(num):
            if(num>=properties[-1][0]):
                return len(properties)
            if(num<properties[0][0]):
                return 0
            
            left = 0
            right = len(properties)-1
            ind = None
            while(left<=right):
                mid = (left+right)//2
                if(properties[mid][0]>num):
                    ind = mid
                    right = mid-1
                else:
                    left = mid+1
            return ind

        for i in range(len(properties)-2, -1, -1):
            attack = properties[i][0]
            defense = properties[i][1]
            ind = bisect_right(attack)
            if(ind<len(properties) and q[ind]>defense):
                ans +=1
        return ans