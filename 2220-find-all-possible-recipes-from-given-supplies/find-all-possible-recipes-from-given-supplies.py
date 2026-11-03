class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set()
        not_possible = set()

        for ing in supplies:
            available.add(ing)

        graph = {}
        for i in range(len(recipes)):
            nde = recipes[i]
            ings = ingredients[i]
            if(nde not in graph):
                graph[nde] = set()
            
            for ing in ings:
                graph[nde].add(ing)
            
        path = set()
        ans = []
        def topo_sort(ing):
            if(ing in path or ing in not_possible):
                return False
            if(ing in available):
                return True

            if(ing not in graph): #i missed this part and got wrong answer
                not_possible.add(ing) #note this is unnecessary, as the path contains the not_possible ings
                return False

            path.add(ing)
            neigh = graph.get(ing, set())
            for nei in neigh:
                if(not topo_sort(nei)):
                    not_possible.add(ing) #note this is unnecessary, as the path contains the not_possible ings
                    return False

            ans.append(ing)
            available.add(ing)
            path.remove(ing)
            return True

        for k in graph.keys():
            if(k not in available):
                topo_sort(k)
        return ans

        