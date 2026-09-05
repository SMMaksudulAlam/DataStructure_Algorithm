import heapq as hq
class uf:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.emails = set()
        self.emails.add(email)
        self.parent = self
    
    def find(self):
        cur = self
        while(cur.parent != cur):
            cur = cur.parent
        parent = cur

        cur = self
        while(cur!=parent):
            temp = cur.parent
            cur.parent = parent
            cur = temp
        return parent

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accs = {}
        parents = set()
        for acc in accounts:
            name = acc[0]
            for i in range(1, len(acc)):
                email = acc[i]
                nde = uf(name, email)
                accs[email] = nde
                parents.add(email)
        #print(accs, parents)

        for acc in accounts:
            email1 = acc[1]
            for i in range(2, len(acc)):
                email2 = acc[i]
                pr1 = accs[email1].find()
                pr2 = accs[email2].find()
                if(pr1 != pr2):
                    if(len(pr1.emails) >= len(pr2.emails)):
                        pr1.emails = pr1.emails.union(pr2.emails)
                        pr2.parent = pr1
                        parents.remove(pr2.email)
                    else:
                        pr2.emails = pr1.emails.union(pr2.emails)
                        pr1.parent = pr2
                        parents.remove(pr1.email)
            
        ans = []
        for p in parents:
            pr = accs[p]
            acc = [pr.name]
            emails = list(pr.emails)
            emails.sort()
            acc += emails
            ans.append(acc)
        return ans

