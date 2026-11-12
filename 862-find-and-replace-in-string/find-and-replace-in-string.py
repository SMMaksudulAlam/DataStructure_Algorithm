class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        input_ = []
        for i in range(len(indices)):
            input_.append((indices[i], sources[i], targets[i]))
        
        input_.sort(key = lambda x:x[0])

        output_ = []
        pos = 0

        for ind, src, tar in input_:
            if(s[ind:ind+len(src)] == src):
                unchanged = s[pos:ind]
                if(unchanged):
                    output_.append(unchanged)
                output_.append(tar)
                pos = ind+len(src)
            else:
                pass
        if(pos<len(s)):
            output_.append(s[pos:])
        
        ans = "".join(output_)
        return ans

        #TC -> O(n)