# adapter pattern
class Queue:
    def __init__(self):
        self.container=list()
        
    def empty(self):
        if not self.container:
            return True
        return False
    
    #래퍼 함수(wrapeer function)
    def enqueue(self, data):
        self.container.append(data)
    
    def dequeue(self):
        return self.container.pop(0)
    
    def peek(self):
        return self.container[0]