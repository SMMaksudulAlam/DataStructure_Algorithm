class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dic = {}
        for w in wordList:
            for i in range(len(w)):
                s = w[:i]+'*'+w[i+1:]
                if(s not in dic):
                    dic[s] = set()
                dic[s].add(w)
        
        count = 1
        visited = set()
        vis = set()
        visited.add(beginWord)
        vis.add(beginWord)

        while(vis):
            vis_ = set()
            for w in vis:
                if(w == endWord):
                    return count
                for i in range(len(w)):
                    s = w[:i]+'*'+w[i+1:]
                    if(s not in dic):
                        continue
                    lst = dic[s]
                    for w_ in lst:
                        if(w_ not in visited):
                            visited.add(w_)
                            vis_.add(w_)
            count+=1
            vis = vis_
        return 0


