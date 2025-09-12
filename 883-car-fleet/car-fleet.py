class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(position)):
            stack.append([position[i], speed[i]])
        
        stack.sort(key = lambda x: x[0])

        count = 0
        while(stack):
            p, s = stack.pop()
            if(not stack):
                count+=1
                break
            if(s>=stack[-1][1]):
                count +=1
            else:
                t = (target-p)/s
                p_, s_ = stack[-1]
                target_ = p_+s_*t
                if(target_>=target):
                    stack[-1] = [p, s]
                else:
                    count+=1

        return count
