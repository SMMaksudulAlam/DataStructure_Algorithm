class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k//2):
            f = x+i
            l = (x+k-1)-i

            for j in range(k):
                cur = y+j
                grid[f][cur], grid[l][cur] = grid[l][cur], grid[f][cur]
        return grid