class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        p2w = {} #track the mapping of pattern to word

        wordList.append(beginWord)
        for w in wordList:
            for i in range(len(w)):
                p = w[:i] + '*' + w[i+1:]
                if(p not in p2w):
                    p2w[p] = []
                p2w[p].append(w)
        #print(p2w)

        words = []

        words.append(beginWord)

        track = {} #tracks the depth and parents
        track[beginWord] = [0, set()]

        while(words):
            #print(words)
            words_ = []
            while(words):
                w = words.pop()
                dist = track[w][0]
                for i in range(len(w)):
                    p = w[:i] + '*' + w[i+1:]
                    wrds = p2w[p]
                    for w_ in wrds:
                        if(w_ not in track):
                            track[w_] = [dist+1, set([w])]
                            words_.append(w_)
                        else:
                            if(track[w_][0] == dist+1):
                                track[w_][1].add(w)
            words = words_
        #print(track)
        if(endWord not in track):
            return []
        

        def traverse(w):
            if(w == beginWord):
                return [[beginWord]]
            
            parents = track[w][1]
            ans = []
            for p in parents:
                ans_ = traverse(p)
                for an in ans_:
                    ans.append(an+[w])
            return ans
        
        ans = traverse(endWord)
        #print(ans)
        return ans
            



