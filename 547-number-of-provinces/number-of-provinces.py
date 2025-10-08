class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(i):
            ln = len(isConnected)
            for j in range(ln):
                if(isConnected[i][j]==1):
                    isConnected[i][j] = 0
                    isConnected[j][i] = 0
                    dfs(j)
            return 
        
        count = 0
        ln = len(isConnected)
        for i in range(ln):
            for j in range(ln):
                if(isConnected[i][j]==1):
                    count+=1
                    dfs(i)
        return count

            
