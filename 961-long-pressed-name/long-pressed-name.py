class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def count(name):
            ans = []
            i = 0
            while(i<len(name)):
                count = 1
                ch = name[i]
                j = i+1
                while(j<len(name) and name[j]==ch):
                    count += 1
                    j+=1
                ans.append((ch, count))
                i = j
            return ans
        
        name_ans = count(name)
        typed_ans = count(typed)

        if(len(name_ans)!=len(typed_ans)):
            return False

        for i in range(len(name_ans)):
            n_c = name_ans[i][0]
            n_f = name_ans[i][1]

            if(typed_ans[i][0]!=n_c or typed_ans[i][1]<n_f):
                return False
        
        return True