class DisjointSet:
    par,rank=[],[]

    def __init__(self,n):
        rank=[0]*n
        for i in range(len(n)):
            self.par.add(i)

    def findParent(self,node):
        if self.par[i]==node:
            return node
        return self.findParent(self.par[node])
    
    def UnionByRank(self,u,v):
        pU=self.findParent(u)
        pV=self.findParent(v)
        if pU==pV:
            return
        if self.rank[pU]==self.rank[pV]:
            self.rank[pU]+=1
            self.parent[pV]=pU
        elif self.rank[pU]>self.rank[pV]:
            self.parent[pV]=pU
        else:
            self.parent[pU]=pV



        

