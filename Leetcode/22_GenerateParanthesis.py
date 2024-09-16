class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        st=[]


        def rec(open,closed):
            if open>=n and closed>=n:
                res.append("".join(st))
            if open<n:
                st.append('(')
                rec(open+1,closed)
                st.pop()
            if closed<open:
                st.append(')')
                rec(open,closed+1)
                st.pop()

            return
            

        

        rec(0,0)
        return res




        


        