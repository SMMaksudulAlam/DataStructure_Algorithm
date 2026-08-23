class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palind(i, j):
            left = i
            right = j

            while(left<=right):
                if(s[left]!=s[right]):
                    return False
                left+=1
                right-=1
            return True

        def build(ind):
            if(ind == len(s)):
                return [[]]
            ans = []
            for i in range(ind, len(s)):
                if(is_palind(ind, i)):
                    temp_str = s[ind:i+1]
                    temp_ans = build(i+1)
                    for e in temp_ans:
                        e = [temp_str] + e
                        ans.append(e)
            return ans
        
        ans = build(0)
        return ans
