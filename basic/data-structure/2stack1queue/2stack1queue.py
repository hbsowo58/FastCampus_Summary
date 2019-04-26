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
# class Queue:
#     def __init__(self):
#         self.first=Stack()
#         self.second=Stack()
        
#     def empty(self):
#         if not self.first:
#             return True
#         elif not self.second:
#             return True
#         else:
#             return False
    
#     def enqueue(self, data):
#         self.first.push(data)
    
#     def dequeue(self):
#         a = empty(self)
#         if self.second == a:
#             shift()
#         else:
#             return self.second.pop(data)
    
#     def peek(self):
#         b = empty(self)
#         if self.second == b:
#             shift()
#         else:
#             return self.second[0]
#     def shift(self):
#         self.second.push(data)
#         self.first.pop(data)
class Queue:
    def __init__(self):
        self.first=Stack()
        self.second=Stack()
        
    def empty(self):
        if self.first.empty() and self.second.empty():
            return True
        return False
    
    def enqueue(self, data):
        self.first.push(data)
    
    def dequeue(self):
        if self.empty():
            return None
        if self.second.empty(): # 이것의 포인트
            while not self.first.empty():
                self.second.push(self.first.pop())
            
        return self.second.pop()


