class Solution:
    def longestDupSubstring(self, s: str) -> str:
        mod = 10**9 + 7
        base = 26
        ans = ""
        
        low = 1
        high = len(s)
        while(low<=high):
            length = (high + low) // 2
            hashes = {}
            sm = 0
            power_val = 1
            for i in range(length):
                digit = ord(s[length-1-i]) - ord('a')
                sm = (sm + (digit * power_val) % mod) % mod
                if(i != length - 1):
                    power_val = (power_val * base) % mod

            hashes[sm] = 0
            left = 0
            right = length
            found = False

            while(right<len(s)):
                digit = ord(s[left]) - ord('a')
                sm = (sm - (digit * power_val) % mod) % mod
                left += 1

                sm = (sm*base)%mod
                digit = ord(s[right]) - ord('a')
                sm = (sm + digit) % mod

                if(sm in hashes):
                    prev = hashes[sm]
                    if(s[prev:prev+length] == s[left: left+length]):
                        ans = s[left:left+length]
                        found = True
                        break
                hashes[sm] = left
                right += 1
            
            if(found):
                low = length + 1
            else:
                high = length - 1
        return ans
