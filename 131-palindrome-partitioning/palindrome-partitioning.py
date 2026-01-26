class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pal(s):
            if(s == s[::-1]):
                return True
            return False

        def build_ans(s):
            ans = []
            if(not s):
                return [[]]
            for i in range(1, len(s)+1):
                part = s[:i]
                if(is_pal(part)):
                    temp_ans = build_ans(s[i:])
                    
                    for ans_ in temp_ans:
                        ans.append([part]+ans_)
            return ans
        
        ans = build_ans(s)

        return ans

            