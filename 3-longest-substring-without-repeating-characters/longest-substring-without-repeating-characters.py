class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        ans = 0
        left = 0
        for right in range(len(s)):
            ch = s[right]
            while(ch in window):
                window.remove(s[left])
                left+=1
            window.add(ch)
            ans = max(ans, len(window))
        return ans

