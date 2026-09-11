class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(len(t)>len(s)):
            return ""
        
        tracker_t = {}
        for ch in t:
            tracker_t[ch] = tracker_t.get(ch, 0) + 1
        
        ans = s+'X'
        left = 0
        for right, ch in enumerate(s):
            if(ch in tracker_t):
                tracker_t[ch] -= 1
            
            while(max(tracker_t.values())<=0):
                if(right-left+1 < len(ans)):
                    ans = s[left:right+1]
                if(s[left] in tracker_t):
                    tracker_t[s[left]] += 1
                left+=1
        return ans if len(ans)<=len(s) else ""