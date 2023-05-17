from MyQueue import MyQueue
class Node(object):
    def __init__(self,data=None,next_node=None):
        self.data=data
        self.next_node=next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_dnoe

    def set_next(self,new_next):
        self.next_dnoe=new_next

class LinkedListBasedQueue(MyQueue):
    def __init__(self, head=None, tail=None):
        self.head=None
        self.length=0
        self.tail=None

    def len(self):
        return self.length

    def first(self):
        if self.is_empty():
            raise ValueError ("Queue is empty!")
        else:
            return self.head.get_data()

    def is_empty(self):
        if self.length==0:
            return True

    def enqueue(self,item):
        new_node=Node(item)
        if self.is_empty():
            self.head=new_node
        else:
            self.tail.next_node=new_node
        self.tail=new_node
        self.length+=1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        if self.length==1:
            self.tail=None
        self.head=self.head.next_node
        self.length-=1

    def printMyQueue(self):
        current=self.head
        while current:
            print(current.get_data(), end=" ")
            current=current.next_node
        print()

my_queue=LinkedListBasedQueue()
my_queue.enqueue(5)
my_queue.enqueue(3)
my_queue.printMyQueue()
print(my_queue.length)
my_queue.dequeue()
my_queue.dequeue()
if my_queue.is_empty():
    print("Queue is empty!")
my_queue.dequeue()
my_queue.enqueue(7)
my_queue.enqueue(9)
print(my_queue.first())