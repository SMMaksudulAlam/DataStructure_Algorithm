class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dic = {}
        def mini_max(left, right, p):
            if(left == right):
                if(p == 1):
                    return nums[left], 0
                else:
                    return 0, nums[left]


            key = (left, right, p)
            if(key in dic):
                return dic[key]

            if(p==1):
                p1, p2 = mini_max(left+1, right, 2)

                p11, p22 = mini_max(left, right-1, 2)

                print(p1, p2, p11, p22)
                if(p1+nums[left]>p11+nums[right]):
                    dic[key] = (p1+nums[left], p2)
                    return p1+nums[left], p2
                else:
                    dic[key] = (p11+nums[right], p22)
                    return p11+nums[right], p22
            if(p==2):
                p1, p2 = mini_max(left+1, right, 1)

                p11, p22 = mini_max(left, right-1, 1)
                
                if(p2+nums[left]>p22+nums[right]):
                    dic[key] = (p1, p2+nums[left])
                    return p1, p2+nums[left]
                else:
                    dic[key] = (p11, p22+nums[right])
                    return p11, p22+nums[right]
            return -1

        p1, p2 = mini_max(0, len(nums)-1, 1)
        return True if(p1>=p2) else False