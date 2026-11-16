class Solution:
    def maximumANDSum(self, nums: list[int], numSlots: int) -> int:
        """
        trie = {}
        length = 4

        #0000
        for n in nums:
            tr = trie
            for i in range(length-1, -1, -1):
                set_bit = 0
                if(n & 1 << i != 0):
                    set_bit = 1
                
                if(set_bit not in tr):
                    tr[set_bit] = {}
                
                tr = tr[set_bit]

            tr[n] = 'end'
        
        ans = []
        for i in range(numSlots):
            ans.append([])


        def dfs(tr, numSlot, i):
            if(i == -1):
                print(tr, numSlot, i)
                key = None
                for k, v in tr.items():
                    key = k
                ans[numSlot-1].append(key)
                del tr[key]
                return
                

            set_bit = 0
            if(numSlot & 1 << i != 0):
                set_bit = 1
            
            found = True
            if(set_bit in tr):
                tr = tr[set_bit]

            else:
                found = False
                tr = tr[1 - set_bit]
            
            if(len(ans[numSlot-1])<2):
                dfs(tr, numSlot, i-1)
            
            if(not tr):
                if(found):
                    del tr[set_bit]
                else:
                    del tr[1 - set_bit]
                return

            found = True
            if(set_bit in tr):
                tr = tr[set_bit]

            else:
                found = False
                tr = tr[1 - set_bit]

            if(len(ans[numSlot-1])<2):
                dfs(tr, numSlot, i-1)

            if(not tr):
                if(found):
                    del tr[set_bit]
                else:
                    del tr[1 - set_bit]
            
            return 

        
        for numSlot in range(numSlots, 0, -1):
            index = numSlot - 1
            tr = trie

            dfs(tr, numSlot, length-1)
        
        return ans
        """
        #i tried it with trie, but the implementation is buggy and it approach does not solve the problem.

        """
        fill = 2**len(nums) - 1

        @lru_cache
        def optimize_sum(ind, occupied, mask):
            if(ind == numSlots):
                if(mask == fill):
                    return 0
                return -math.inf

            if(mask == fill):
                return 0
            ans = optimize_sum(ind+1, 0, mask)

            for i in range(len(nums)):
                if(mask & 1 << i == 0):
                    mask |= 1 << i
                    if(occupied == 0):
                        ans = max(ans, (nums[i] & (ind+1)) + optimize_sum(ind, occupied+1, mask))
                    ans = max(ans, (nums[i] & (ind+1)) + optimize_sum(ind+1, 0, mask))
                    mask ^= 1 << i
            return ans
        
        ans = optimize_sum(0, 0, 0)
        return ans

        """

        
        @lru_cache(None)
        def optimize_sum(num_ind, mask):

            if(num_ind == len(nums)):
                return 0

            ans = 0
            for i in range(len(mask)):
                if(mask[i] > 0):
                    mask_array = list(mask)
                    mask_array[i] -= 1
                    mask_tuple = tuple(mask_array)
                    ans = max(ans, (nums[num_ind] & (i+1)) + optimize_sum(num_ind+1, mask_tuple))

            return ans

        mask = tuple([2]*numSlots)
        ans = optimize_sum(0, mask)
        return ans