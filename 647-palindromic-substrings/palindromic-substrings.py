class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            left = i
            right = i
            while(left>=0 and right<len(s) and s[left]==s[right]):
                left-=1
                right+=1
                count+=1
            
            if(i>0 and s[i-1]==s[i]):
                left = i-1
                right = i
                while(left>=0 and right<len(s) and s[left]==s[right]):
                    left-=1
                    right+=1
                    count+=1

        return count
            

