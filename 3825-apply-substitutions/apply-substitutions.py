class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        resolved = {}
        not_resolved = {}

        for k, v in replacements:
            if('%' not in v):
                resolved[k] = v
                continue
            else:
                not_resolved[k] = v.split('%')
            
        #track = set() #no cycles

        def dfs(k):
            if(k in resolved):
                return resolved[k]
            s = ""
            for p in not_resolved[k]:
                if(p in not_resolved or p in resolved):
                    s+=dfs(p)
                else:
                    s+=p
            del not_resolved[k]
            resolved[k] = s
            return s
        
        lst = list(not_resolved.keys())
        for k in lst:
            if(k in not_resolved):
                dfs(k)
        
        text_list = text.split('%')
        ans = ""
        for p in text_list:
            if(p in resolved):
                ans+=dfs(p)
            else:
                ans+=p
        return ans


    