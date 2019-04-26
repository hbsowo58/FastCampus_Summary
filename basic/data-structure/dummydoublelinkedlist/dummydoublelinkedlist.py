class Node:
    def __init__(self, data=None):
        self.prev=None
        self.data=data
        self.next=None
    
    #객체가 소멸될때
    #반드시 한번 호출된다
    def __del__(self):
        print(f'{self.data} is deleted')
class DLinkedList:
    def __init__(self):
        self.head=Node()
        self.tail=Node()
        self.d_size = 0
        
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def empty(self):
        if self.d_size==0:
            return True
        return False
    
    def size(self):
        return self.d_size
    
    def add_first(self, data):
        #새로운 노드를 만들었다!!
        new_node=Node(data)
        
        
        #new_node 기준에서 연결
        new_node.prev=self.head
        new_node.next=self.head.next
        
        self.head.next.prev=new_node
        self.head.next=new_node
        
        self.d_size+=1
        
    def add_last(self,data):
        
        new_node=Node(data)
        
        new_node.next=self.tail
        new_node.prev=self.tail.prev
        
        self.tail.prev.next=new_node
        self.tail.prev=new_node
        
        self.d_size+=1
        
    def insert_after(self, data, node):
        
        new_node=Node(data)
        
        new_node.prev=node
        new_node.next=node.next
        
        node.next.prev=new_node
        node.next=new_node
        
        self.d_size+=1
    
    def insert_before(self, data, node):
        
        new_node=Node(data)
        
        new_node.prev=node.prev
        new_node.next=node
        
        node.prev.next=new_node
        node.prev=new_node
        
        self.d_size+=1
    
    def search_forward(self, target):
        cur = self.head.next
        
        while cur is not self.tail:
            if cur.data==target:
                return cur
            cur=cur.next
            
        return None
    
    def search_backward(self, target):
        cur = self.tail.prev
        
        while cur is not self.head:
            if cur.data==target:
                return cur
            cur=cur.prev
            
        return None    
        

    def delete_first(self):
        if self.empty():
            return
        
        self.head.next=self.head.next.next
        self.head.next=self.head
        
        self.d_size-=1
        
    def delete_last(self):
        if self.empty():
            return
        
        self.tail.prev=self.tail.prev.prev
        self.tail.prev.next=self.tail
        
        self.d_size-=1
        
    def delete_node(self, node):
        if self.empty():
            return
        
        node.next.prev=node.prev
        node.prev.next=node.next
        
        self.d_size-=1
        
#제너레이터        
def show_list(dlist):
    cur=dlist.head.next
    while cur is not dlist.tail:
        yield cur.data
        cur=cur.next