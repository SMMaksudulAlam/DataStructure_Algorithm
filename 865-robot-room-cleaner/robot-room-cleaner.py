# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        dir = [('u', (0, 1)), ('r', (1, 0)), ('d', (0, -1)), ('l', (-1, 0))]
        ind_map = {'u': 0, 'r': 1, 'd': 2, 'l': 3}

        x = 0
        y = 0
        d = 'u'

        visited = set()

        def dfs(x, y, d):
            robot.clean()
            visited.add((x, y))

            ind = ind_map[d]

            for i in range(4):
                next_dir, val = dir[(ind+i)%4]
                next_x = x+val[0] 
                next_y = y+val[1] 

                if((next_x, next_y) not in visited):
                    if(robot.move()): 
                        dfs(next_x, next_y, next_dir)
                        robot.turnLeft()
                    else:
                        robot.turnRight()
                else:       
                    robot.turnRight()

            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            return
        
        dfs(x, y, d)



