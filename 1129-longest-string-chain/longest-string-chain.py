class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wrds = []
        for w in words:
            wrds.append((len(w), w))
        
        wrds.sort(key = lambda x: x[0])
        
        ln = wrds[0][0]
        ans = []
        i = 0
        while(i<len(wrds) and wrds[i][0]==ln):
            ans.append(1)
            i+=1
        
        #print(wrds, ans)
        
        pre_len = ln
        ind = i
        while(ind<len(wrds)):
            if(pre_len+1 == wrds[ind][0]):
                s = wrds[ind][1]
                pre_ind = ind-1
                while(pre_ind>=0 and wrds[pre_ind][0]>=pre_len):
                    if(wrds[pre_ind][0]==pre_len):
                        pre = wrds[pre_ind][1]
                        count = 0
                        x = 0
                        for y in range(len(s)):
                            if(count == len(pre)):
                                break
                            if(pre[x]==s[y]):
                                count+=1
                                x+=1
                        if(count == wrds[pre_ind][0]):
                            if(len(ans)==ind):
                                ans.append(ans[pre_ind]+1)
                            else:
                                ans[-1] = max(ans[-1], ans[pre_ind]+1)
                        else:
                            if(len(ans)==ind):
                                ans.append(1)
                    pre_ind-=1
                   #print(s, ans)
                ind+=1

            else:
                if(wrds[ind][0] - pre_len > 2):
                    break
                if(wrds[ind][0] - pre_len == 2):
                    pre_len += 1
        return max(ans)