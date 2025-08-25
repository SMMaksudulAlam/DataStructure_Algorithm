class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
        dic = {}
        for x, y in dominoes:
            if((x, y) in dic):
                dic[(x, y)] += 1
            elif((y, x) in dic):
                dic[(y, x)] += 1
            else:
                dic[(x, y)] = 1
        
        count = 0
        for v in dic.values():
            if(v>1):
                count += (v*(v-1))//2
        return count