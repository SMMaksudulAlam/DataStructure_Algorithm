class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = ""
        for e in s:
            if(e.isalnum()):
                s_+=e.lower()
        return s_[::-1]==s_