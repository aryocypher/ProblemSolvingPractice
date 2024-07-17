class Solution:
    def knapSackRec(self, N, W, val, wt):
        cache={}
        
        
        def rec(i,currW):
            if i>=N or currW<=0:
                return 0
            if (i,currW) in cache:
                return cache[(i,currW)]
            inc1=0
            inc2=0
            exc=0
            if currW>=wt[i]:
                inc1=val[i]+rec(i+1,currW-wt[i])
                inc2=val[i]+rec(i,currW-wt[i])
            exc=rec(i+1,currW)
            
            
            cache[(i,currW)]= max(inc1,inc2,exc)
            return cache[(i,currW)]
        return rec(0,W)
    
    def knapSackIte(self, N, W, val, wt):
        cache=[[0 for i in range(W+1)] for j in range(N+1)]
        
        for i in range(N+1):
            for j in range(W+1):
                inc1=0
                inc2=0
                exc=0
                if j>=wt[i-1]:
                    inc1=val[i-1]+cache[i][j-wt[i-1]]
                    inc2=val[i-1]+cache[i-1][j-wt[i-1]]
                    
                exc=cache[i-1][j]
                cache[i][j]=max(inc1,inc2,exc)
        return cache[N][W]
        