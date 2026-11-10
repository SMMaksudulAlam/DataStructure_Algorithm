class Solution:
    def wordCount(self, startWords: list[str], targetWords: list[str]) -> int:
        dic = {}
        mask = set()
        for w in targetWords: # a c k t
            w_mask = 0
            for ch in w:
                ind = ord(ch) - ord('a')
                w_mask |= 1 << ind
                mask.add(ind)
            dic[w_mask] = dic.get(w_mask, 0) + 1
        
        ans = 0
        for w in startWords:
            w_mask = 0
            for ch in w:
                ind = ord(ch) - ord('a')
                w_mask |= 1 << ind
            # a c t
            for i in mask: #in the inefficient version, i loop over 0-25, but we can store the required index in mask set and only work on them
                temp_w_mask = w_mask
                if(temp_w_mask & 1<<i == 0): #a c k t
                    temp_w_mask |= 1<<i 
                    ans += dic.get(temp_w_mask, 0)
                    if(temp_w_mask in dic): #i missed this part in the first version
                        del dic[temp_w_mask]
        return ans