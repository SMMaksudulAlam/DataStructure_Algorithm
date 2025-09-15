class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        for i in range(len(s)):
            left = i
            right = i

            while(left>=0 and right<len(s) and s[left]==s[right]):
                left-=1
                right+=1
            
            p = s[left+1:right]
            if(len(p)>len(ans)):
                ans = p
            
            if(i>0 and s[i-1]==s[i]):
                left = i-1
                right = i

                while(left>=0 and right<len(s) and s[left]==s[right]):
                    left-=1
                    right+=1

                p = s[left+1:right]
                if(len(p)>len(ans)):
                    ans = p
        return ans

