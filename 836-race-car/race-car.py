class Solution:
    def racecar(self, target: int) -> int:
        dic = {}
        pos = 0
        speed = 1
        count = 0

        while(pos+speed <= target):
            count += 1
            if(pos+speed == target):
                return count
            pos += speed
            speed *= 2
            dic[pos] = count

        count += 1 #i missed the line
        pos += speed
        speed *= 2
        dic[pos] = count #{1: 1, 3: 2, 7: 3}

        lst = list(dic.keys()) #[1, 3, 7]
        #print(lst)

        def mini_step(target): #6 2
            if(target in dic):
                return dic[target]
            
            ind = bisect.bisect_left(lst, target) #2 1
            over_pos = lst[ind] # 7 3
            under_pos = lst[ind-1] # 3 1

            over_ans = dic[over_pos] + 1 + mini_step(over_pos - target) # 3 + 1 + 1 = 5 | 2 + 1 + 1 = 3
            under_ans = dic[under_pos] + 2 + mini_step(target - under_pos) # 2 + 2 + mini_step(2) = 8 |  1 + 2 + 1 = 4

            sp = 1
            other_under_pos = under_pos # 1 | 3
            i = 1

            if(target == 6):
                print(ind, over_pos, under_pos, over_ans, under_ans, other_under_pos)
            while(True):
                other_under_pos -= sp # 0 # 2
                if(other_under_pos <= 1): 
                    break
                other_under_ans = dic[under_pos] + 2 + i + mini_step(target - other_under_pos) # 2 + 2 + 1 + 1
                sp *= 2
                i += 1
                under_ans = min(under_ans, other_under_ans)
            
            ans = min(over_ans, under_ans)
            dic[target] = ans
            #print("here", dic)
            return ans

        return mini_step(target)