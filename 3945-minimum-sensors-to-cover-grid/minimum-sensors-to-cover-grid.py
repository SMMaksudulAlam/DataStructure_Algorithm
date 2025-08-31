class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        if(k==0):
            return m*n

        count = 1
        
        perRow = m//(2*k+1)
        if(m%(2*k+1)!=0):
            perRow+=1
        
        perCol = n//(2*k+1)
        if(n%(2*k+1)!=0):
            perCol+=1

        
        
        return perCol*perRow
        
