class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    
    def find(self,x):
        if x!=self.parents[x]:
            self.parents[x] =self.find(self.parents[x])
        return self.parents[x]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))

        #creater unions between indices
        ownership = {}
        for i, (_,*emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i,ownership[email])
                ownership[email]=i

        #append emails to correct index
        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)

        return [[accounts[i][0]]+sorted(emails) for i,emails in ans.items()]