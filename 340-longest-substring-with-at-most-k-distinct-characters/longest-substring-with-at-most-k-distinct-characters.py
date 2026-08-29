class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if(k==0):
            return 0
        count = {}
        left = 0
        ans = 0
        for right in range(len(s)):
            if(s[right] not in count):
                while(len(count.keys())>=k):
                    count[s[left]] -= 1
                    if(count[s[left]] == 0):
                        del count[s[left]]
                    left+=1
            count[s[right]] = count.get(s[right], 0)+1
            ans = max(ans, right-left+1)
        return ans