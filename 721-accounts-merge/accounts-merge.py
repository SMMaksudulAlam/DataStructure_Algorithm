import heapq as hq

class uf:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.childs = set()
        self.childs.add(id)

    def find(self):
        while(self != self.parent):
            self = self.parent
        return self

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dic = {}
        parent = set()
        emails = {}

        for acc_no in range(len(accounts)):
            acc = accounts[acc_no]
            dic[acc_no] = uf(acc_no)
            parent.add(acc_no)

            for i in range(1, len(acc)):
                eml = acc[i]
                if(eml in emails):
                    another_acc = dic[emails[eml]]
                    another_acc_parent = another_acc.find()
                    my_acc_parent = dic[acc_no].find()

                    if(another_acc_parent == my_acc_parent):
                        continue

                    if(len(another_acc_parent.childs)>len(my_acc_parent.childs)):
                        my_acc_parent.parent = another_acc_parent
                        parent.remove(my_acc_parent.id)
                        for child in my_acc_parent.childs:
                            another_acc_parent.childs.add(child)
                    else:
                        another_acc_parent.parent = my_acc_parent.parent
                        parent.remove(another_acc_parent.id)
                        for child in another_acc_parent.childs:
                            my_acc_parent.childs.add(child)

                emails[eml] = acc_no
        
        ans = []
        for p in parent:
            acc = dic[p]
            name = accounts[p][0]
            emails = set()
            for ch in acc.childs:
                for eml in accounts[ch][1:]:
                    emails.add(eml)
            emails = list(emails)
            emails.sort()
            lst = [name] + emails
            ans.append(lst)
        return ans
