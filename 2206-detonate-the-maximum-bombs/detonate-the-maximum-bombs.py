"""
class uf:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.count = 1
    
    def find(self):
        parent = self
        while(parent != parent.parent):
            parent = parent.parent
        
        curr = self
        while(curr!=parent):
            temp = curr.parent
            curr.parent = parent
            curr = temp

        return parent


class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        nodes = {}
        parents = set()

        def overlaps(ind1, ind2):
            cir1 = bombs[ind1]
            cir2 = bombs[ind2]

            dis = math.sqrt((cir1[0]-cir2[0])**2 + (cir1[1]-cir2[1])**2)
            max_rad = max(cir1[2], cir2[2])  # to detonate, overlap is not enough, the center of a circle should reside in the range of other one.

            return True if max_rad>=dis else False


        for i in range(len(bombs)):
            nodes[i] = uf(i)
            parents.add(i)
        
        for i in range(len(bombs)):
            nde1 = nodes[i]
            for j in range(i+1, len(bombs)):
                if(overlaps(i, j)):
                    nde2 = nodes[j]
                    
                    pr1 = nde1.find()
                    pr2 = nde2.find()
                    if(pr1 == pr2):
                        continue
                    
                    if(pr1.count>=pr2.count):
                        pr1.count += pr2.count
                        pr2.parent = pr1
                        parents.remove(pr2.id)
                    else:
                        pr2.count += pr1.count
                        pr1.parent = pr2
                        parents.remove(pr1.id)

        ans = 1
        for p in parents:
            ans = max(ans, nodes[p].count)
        #print(parents, len(bombs))
        return ans

"""
### this is a directed graph where union-find is not applicable

class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:

        def overlaps(ind1, ind2):
            cir1 = bombs[ind1]
            cir2 = bombs[ind2]
            edges = []

            dis = math.sqrt((cir1[0]-cir2[0])**2 + (cir1[1]-cir2[1])**2)
            max_rad = max(cir1[2], cir2[2])

            if(dis <= max_rad):
                if(dis <= cir1[2]):
                    edges.append((ind1, ind2))
                if(dis <= cir2[2]):
                    edges.append((ind2, ind1))
            return edges

        path = set()
        def dfs(nde):
            if(nde in path):
                return 0
            count = 1
            path.add(nde)
            neigh = graph.get(nde, [])
            max_len = 0
            for n in neigh:
                count += dfs(n)
            return count

        ans = 1
        graph = {}
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                edges = overlaps(i, j)
                for u, v in edges:
                    if(u not in graph):
                        graph[u] = set()
                    graph[u].add(v)
        
        #print(graph)
        for k in graph.keys():
            path = set()
            ans = max(ans, dfs(k))
        return ans