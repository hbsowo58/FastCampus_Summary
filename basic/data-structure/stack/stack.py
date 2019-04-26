# adapter pattern
class Stack:
    def __init__(self):
        self.container=list()
        
    def empty(self):
        if not self.container:
            return True
        return False
    
    #래퍼 함수(wrapeer function)
    def push(self, data):
        self.container.append(data)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]