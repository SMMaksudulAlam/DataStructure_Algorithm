class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def build(temp, rest):
            if(not rest):
                ans.append(temp) 
            ln = len(rest)
            for i in range(ln):
                x = rest.pop(0)
                build(temp+[x], rest[:])
                rest.append(x)

        build([], nums)
        return ans
