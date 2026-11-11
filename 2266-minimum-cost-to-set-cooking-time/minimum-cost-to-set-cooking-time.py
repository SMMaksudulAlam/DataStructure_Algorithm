class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def press_hr(hr, startAt):
            cost = 0
            if(hr == 0):
                return 0, startAt
            elif(hr <= 9):
                if(hr == startAt):
                    pass
                else:
                    cost += moveCost
                cost+= pushCost
                return cost, hr
            else:
                f_digit = hr // 10
                if(f_digit == startAt):
                    pass
                else:
                    cost += moveCost
                cost += pushCost
                s_digit = hr % 10
                if(s_digit == f_digit):
                    pass
                else:
                    cost += moveCost
                cost += pushCost
                return cost, s_digit
            return 0, 0
        
        def press_min(mins, hr, startAt):
            cost = 0
            if(hr == 0):
                return press_hr(mins, startAt)
            else:
                f_digit = mins // 10
                if(f_digit == startAt):
                    pass
                else:
                    cost += moveCost
                cost += pushCost

                s_digit = mins % 10
                if(s_digit == f_digit):
                    pass
                else:
                    cost += moveCost
                cost += pushCost
                return cost, s_digit
            return 0, 0



        ans = math.inf
        maxi_hr = targetSeconds // 60
        mini_min = targetSeconds % 60

        if(maxi_hr <= 99):
            temp_cost = 0
            cst, next_start = press_hr(maxi_hr, startAt)
            temp_cost += cst
            cst, next_start = press_min(mini_min, maxi_hr, next_start)
            temp_cost += cst
        
            ans = temp_cost
            if(maxi_hr-1>=0 and mini_min+60<=99):
                maxi_hr -= 1
                mini_min += 60
                temp_cost = 0
                cst, next_start = press_hr(maxi_hr, startAt)
                temp_cost += cst
                cst, next_start = press_min(mini_min, maxi_hr, next_start)
                temp_cost += cst
            
                ans = min(ans, temp_cost)
        else:
            maxi_hr -= 1
            mini_min += 60
            temp_cost = 0
            cst, next_start = press_hr(maxi_hr, startAt)
            temp_cost += cst
            cst, next_start = press_min(mini_min, maxi_hr, next_start)
            temp_cost += cst
        
            ans = min(ans, temp_cost)

        return ans

        