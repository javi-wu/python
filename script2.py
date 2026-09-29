class Person:
    def __init__(self):
        self.stack=[]
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None
