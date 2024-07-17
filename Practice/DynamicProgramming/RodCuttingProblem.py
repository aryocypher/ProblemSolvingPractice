class Solution:
    def cutRod(self, price, n):
        #code here
        cache={}
        l=len(price)
        
        def rec(i,j):
            if i>n or j<=0:
                return 0
            
            if (i,j) in cache:
                return cache[(i,j)]
            inc1=0
            exc=0
            inc2=0
            if i<=j:
                inc1=price[i-1]+rec(i+1,j-i)
                inc2=price[i-1]+rec(i,j-i)
            exc=rec(i+1,j)
            cache[(i,j)]= max(inc1,inc2,exc)
            return cache[(i,j)]
            
        return rec(1,n)