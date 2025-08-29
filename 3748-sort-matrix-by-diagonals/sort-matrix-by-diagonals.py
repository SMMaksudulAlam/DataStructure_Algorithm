class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        ln = len(grid)

        for r in range(ln):
            i = r
            j = 0
            lst = []
            while(i<ln and j<ln):
                lst.append(grid[i][j])
                i+=1
                j+=1
            lst.sort()
            i = r
            j = 0
            l = len(lst)
            while(i<ln and j<ln):
                grid[i][j] = lst[l-1-j]
                i+=1
                j+=1

        for c in range(1, ln):
            i = 0
            j = c
            lst = []
            while(i<ln and j<ln):
                lst.append(grid[i][j])
                i+=1
                j+=1
            lst.sort()
            i = 0
            j = c
            l = len(lst)
            while(i<ln and j<ln):
                grid[i][j] = lst[i]
                i+=1
                j+=1
        return grid