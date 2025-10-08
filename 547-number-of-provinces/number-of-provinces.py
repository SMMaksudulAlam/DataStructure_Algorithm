class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        st = set()
        def dfs(i):
            st.add(i)
            ln = len(isConnected)
            for j in range(ln):
                if(isConnected[i][j]==1 and j not in st):
                    dfs(j)
            return 
        
        count = 0
        ln = len(isConnected)
        for i in range(ln):
            for j in range(ln):
                if(isConnected[i][j]==1 and j not in st):
                    st.add(i)
                    count+=1
                    dfs(j)
        return count

            
