class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=['*','/','+','-']
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                oper2=stack.pop()
                oper1=stack.pop()
                if i=='*':
                    res=oper2*oper1
                elif i=='/':
                    res=int(oper1/oper2)
                elif i=='-':
                    res=oper1-oper2
                else:
                    res=oper1+oper2
                stack.append(res)
        return stack[0]
        
            

        