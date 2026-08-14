class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if(len(words)==1):
            ans = list(set([ch for ch in words[0]]))
            return "".join(ans)


        graph = {}
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            for ch in w1:
                if(ch not in graph):
                    graph[ch] = set()
            for ch in w2:
                if(ch not in graph):
                    graph[ch] = set()

            len1 = len(w1) 
            len2 = len(w2)

            if(len1>len2 and w1[:len2] == w2):
                return ""

            mn_ln = min(len1, len2)

            for j in range(mn_ln):
                if(w1[j] != w2[j]):
                    graph[w1[j]].add(w2[j])
                    break
            
        #print(graph)

        completed = set()
        ans = []
        in_path = set()

        def traverse(nde):
            if(nde in in_path):
                return False
            if(nde in completed):
                return True

            in_path.add(nde)
            neigh = graph.get(nde, [])

            for n in neigh:
                if(not traverse(n)):
                    return False

            completed.add(nde)
            ans.append(nde)
            in_path.remove(nde)

            return True

        for nde in graph.keys():
            if(not traverse(nde)):
                return ""

        ans = "".join(ans)
        return ans[::-1]