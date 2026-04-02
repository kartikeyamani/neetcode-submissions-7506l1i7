class MinStack:

    def __init__(self):
        self.temp_stack=[]
        self.mini_stack=[]
        

    def push(self, val: int) -> None:
        self.temp_stack.append(val)
        if not self.mini_stack:
            self.mini_stack.append(val)
        elif val<self.mini_stack[-1]:
            self.mini_stack.append(val)
        else:
            newval=self.mini_stack[-1]
            self.mini_stack.append(newval)
            
        

    def pop(self) -> None:
        self.temp_stack.pop()
        self.mini_stack.pop()
        

    def top(self) -> int:
        return self.temp_stack[-1]
        

    def getMin(self) -> int:
        return self.mini_stack[-1]

        
