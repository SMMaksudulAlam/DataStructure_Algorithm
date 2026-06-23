class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        dic = {}
        ans = 0

        for right in range(len(s)):
            e = s[right]
            dic[e] = dic.get(e, 0)+1

            max_count = max(dic.values())
            rest = (right - left + 1) - max_count

            while(rest>k):
                e = s[left]
                dic[e] -= 1
                left += 1

                max_count = max(dic.values())
                rest = (right - left + 1) - max_count
            
            ans = max(ans, right - left + 1)
        
        return ans