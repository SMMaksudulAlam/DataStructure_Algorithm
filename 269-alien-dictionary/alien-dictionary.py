class Solution:
    def alienOrder(self, words: List[str]) -> str:
        dic = {}
        for w in words:
            for ch in w:
                dic[ch] = set()

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            if(len(w1)>len(w2) and w1[:len(w2)]==w2):
                return ""
            
            for j in range(len(w1)):
                if(w1[j]!=w2[j]):
                    dic[w1[j]].add(w2[j])
                    break
        
        track = set()
        ordered = set()
        ans = []

        def dfs(ch):
            if(not dic[ch]):
                if(ch not in ordered):
                    ordered.add(ch)
                    ans.append(ch)
                return True

            if(ch in track):
                return False
            
            track.add(ch)

            for ch_ in dic[ch]:
                if(not dfs(ch_)):
                    return False

            if(ch not in ordered):
                ordered.add(ch)
                ans.append(ch)
            track.remove(ch)
            return True
        
        for k in dic.keys():
            if(k not in ordered):
                if(not dfs(k)):
                    return ""
        s = "".join(ans)
        return s[::-1]


        
        