class Solution:
    def visiblePoints(self, points: list[list[int]], angle: int, location: list[int]) -> int:
        
        angles = []
        px, py = location
        self_count = 0
        for (x, y) in points:
            if(x == px and y == py):
                self_count += 1
                continue
            angl = math.degrees(math.atan2(y-py, x-px)) % 360
            angles.append(angl)
            #print(x, y, angl)

        angles.sort()
        i = 0
        ln = len(angles)
        while(i<ln and angles[i]<=angle):
            angles.append(360 + angles[i])
            i+=1
        
        #print(angles)

        ans = 0
        left = 0
        right = 0
        
        while(right<len(angles)):
            while(angles[right]-angles[left]>angle):
                left+=1
            ans = max(ans, right-left+1)
            right += 1

        return ans + self_count
            