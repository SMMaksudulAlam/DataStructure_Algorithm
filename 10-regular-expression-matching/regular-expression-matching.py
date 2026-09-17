class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def match(ind_s, ind_p):
            if((ind_s, ind_p) in dp):
                return dp[(ind_s, ind_p)]
            if(ind_s<0):
                if(ind_p<0):
                    return True
                if(ind_p%2==1):
                    for x in range(0, ind_p, 2):
                        if(p[x+1]!='*'):
                            return False
                    return True
                return False
            if(ind_p<0):
                return False
            
            if(p[ind_p] == s[ind_s] or p[ind_p] == '.'):
                dp[(ind_s, ind_p)] =  match(ind_s-1, ind_p-1)
            elif(p[ind_p] == '*'):
                dir1 = match(ind_s, ind_p-2)
                dir2 = False
                if(ind_p>0 and (p[ind_p-1] == '.' or s[ind_s] == p[ind_p-1])):
                    dir2 = match(ind_s-1, ind_p)
                dp[(ind_s, ind_p)] = dir1 or dir2
            else:
                dp[(ind_s, ind_p)] = False
            return dp[(ind_s, ind_p)]
        
        return match(len(s)-1, len(p)-1)