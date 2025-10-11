import heapq as hq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.h = []
        self.dic = {}
        for u_id, t_id, p in tasks:
            hq.heappush(self.h, (-p, -t_id, u_id))
            self.dic[t_id] = (p, u_id)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        hq.heappush(self.h, (-priority, -taskId, userId))
        self.dic[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.dic[taskId][1]
        self.dic[taskId] = (newPriority, userId)
        hq.heappush(self.h, (-newPriority, -taskId, userId))
        

    def rmv(self, taskId: int) -> None:
        del self.dic[taskId]

    def execTop(self) -> int:
        while(self.h):
            priority, taskId, userId = hq.heappop(self.h)
            priority = -priority
            taskId = -taskId
            if(self.dic and taskId in self.dic and self.dic[taskId][0] == priority and self.dic[taskId][1] == userId):
                del self.dic[taskId]
                return userId
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()