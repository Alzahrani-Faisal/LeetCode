class Solution:
    def isValid(self, s: str) -> bool:
        st =[]
        for c in s:
            
            if c == '(' or c == '[' or c == '{':
                st.append(c)
            elif (c== ')' or c == ']' or c == '}') and len(st)!=0:
                if c == ')' and st[len(st)-1] == '(':
                    st.pop()
                elif c == ']' and st[len(st)-1] == '[':
                    st.pop()
                elif c == '}' and st[len(st)-1] == '{':
                    st.pop()
                else:
                    return False
            else:
                return False
        if len(st) == 0:
            return True
        else:
            return False
