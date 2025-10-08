class uf:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.parent = self
        self.count = 1

    def find(self):
        while(self!=self.parent):
            self = self.parent
        return self


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dic = {}
        parent = set()
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        ans = []
        for i, j in positions:
            if((i, j) in dic):
                ans.append(len(parent))
                continue
            
            dic[(i, j)] = uf(i, j)
            parent.add((i, j))
            for dx, dy in dir:
                x = i+dx
                y = j+dy

                if((x, y) in dic):
                    cur_node = dic[(i, j)]
                    neigh_node = dic[(x, y)]

                    cur_node_parent = cur_node.find()
                    neigh_node_parent = neigh_node.find()

                    if(cur_node_parent == neigh_node_parent):
                        continue
                    
                    if(cur_node_parent.count >= neigh_node_parent.count):
                        cur_node_parent.count += neigh_node_parent.count
                        parent.remove((neigh_node_parent.parent.i, neigh_node_parent.parent.j))
                        neigh_node_parent.parent = cur_node_parent
                        

                    else:
                        neigh_node_parent.count += cur_node_parent.count
                        parent.remove((cur_node_parent.parent.i, cur_node_parent.parent.j))
                        cur_node_parent.parent = neigh_node_parent
            ans.append(len(parent))
        return ans
