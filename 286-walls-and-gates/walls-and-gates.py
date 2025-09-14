class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        dir = [(-1, 0), (1, 0), (0, -1,), (0, 1)]

        s = set()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if(rooms[i][j]==0):
                    s.add((i, j))
        
        while(s):
            s_ = set()
            for i, j in s:
                for dx, dy in dir:
                    x = i+dx
                    y = j+dy
                    if(0<=x<len(rooms) and 0<=y<len(rooms[0]) and rooms[x][y]!=-1 and rooms[x][y]>rooms[i][j]+1):
                        rooms[x][y] = rooms[i][j]+1
                        s_.add((x, y))
            s = s_
        return rooms
