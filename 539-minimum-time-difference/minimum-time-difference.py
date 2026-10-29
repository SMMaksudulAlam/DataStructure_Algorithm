class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        ans = math.inf

        timePoints.sort()

        for i in range(1, len(timePoints)):
            left = timePoints[i-1].split(':')
            right = timePoints[i].split(':')

            left_h = int(left[0])
            left_min = int(left[1])

            right_h = int(right[0])
            right_min = int(right[1])

            temp_ans = ans
            if(left_h < right_h):
                temp_ans = 60-left_min
                left_h += 1
                temp_ans += (right_h-left_h)*60
                temp_ans += right_min
            else:
                temp_ans = right_min - left_min
            
            ans = min(ans, temp_ans)

        left = timePoints[-1].split(':')
        left_h = int(left[0])
        left_min = int(left[1])
        temp_ans = 60-left_min
        left_h += 1
        temp_ans += (24-left_h)*60

        right = timePoints[0].split(':')
        right_h = int(right[0])
        right_min = int(right[1])
        temp_ans += (right_h)*60
        temp_ans += right_min

        ans = min(ans, temp_ans)
        return ans