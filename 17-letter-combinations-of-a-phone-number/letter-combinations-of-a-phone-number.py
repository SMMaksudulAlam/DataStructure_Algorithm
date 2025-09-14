class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(digits==""):
            return []
        dic = {}
        dic['2'] = 'abc' 
        dic['3'] = 'def' 
        dic['4'] = 'ghi' 
        dic['5'] = 'jkl' 
        dic['6'] = 'mno' 
        dic['7'] = 'pqrs' 
        dic['8'] = 'tuv' 
        dic['9'] = 'wxyz' 
       
        ans = [""]
        for d in digits:
            chrs = dic[d]
            temp = []
            for c in chrs:
                for a in ans:
                    temp.append(a+c)
            ans = temp
        return ans

