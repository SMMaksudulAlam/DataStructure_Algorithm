class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def build(r, dic):
            nonlocal n
            if(r==n):
                ans1 = [['.']*n for _ in range(n)]
                for r_, c_ in dic.keys():
                    ans1[r_][c_] = 'Q'
                ans.append(ans1)
                return
            for c in range(n):
                r_ = r
                c_ = c
                conflict = False
                while(r_>=0):
                    if((r_, c_) in dic):
                        conflict = True
                        break
                    r_-=1
                if(conflict):
                    continue
                r_ = r
                c_ = c
                while(r_>=0 and c_>=0):
                    if((r_, c_) in dic):
                        conflict = True
                        break
                    r_-=1
                    c_-=1

                if(conflict):
                    continue
                r_ = r
                c_ = c
                while(r_>=0 and c_<n):
                    if((r_, c_) in dic):
                        conflict = True
                        break
                    r_-=1
                    c_+=1
                
                if(conflict):
                    continue

                dic[(r, c)] = 1
                build(r+1, dic)
                del dic[(r, c)]


        for c in range(n):
            build(1, {(0, c):1})

        ans_str = []
        for ans_ar in ans:
            sol = []
            for row in ans_ar:
                r = "".join(row)
                sol.append(r)
            ans_str.append(sol)
        return ans_str
