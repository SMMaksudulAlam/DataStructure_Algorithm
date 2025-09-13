class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if(slow==fast):
                break
        
        slowN = 0
        while True:
            slow = nums[slow]
            slowN = nums[slowN]
            if(slow == slowN):
                return slow
        return -1