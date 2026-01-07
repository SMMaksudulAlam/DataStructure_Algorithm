class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ans = ""
        while(words):
            ans+=words.pop()
            if(words):
                ans+=" "
        return ans