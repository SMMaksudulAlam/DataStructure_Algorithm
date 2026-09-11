class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
            return False
        
        track_s1 = [0]*26
        for ch in s1:
            ind = ord(ch) - ord('a')
            track_s1[ind]+=1
        
        track_s2 = [0]*26
        left = 0
        
        for right in range(len(s2)):
            ch = s2[right]
            ind = ord(ch) - ord('a')
            track_s2[ind] += 1
            while(track_s2[ind] > track_s1[ind]):
                ch_ = s2[left]
                ind_ = ord(ch_) - ord('a')
                track_s2[ind_] -= 1
                left += 1
            
            matched = True
            for ind in range(26):
                if(track_s2[ind] != track_s1[ind]):
                    matched = False
                    break
            if(matched):
                return True
        return False