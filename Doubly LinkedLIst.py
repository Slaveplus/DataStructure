from MyList import MyList
class Node(object):
    def __init__ (self,data=None,next_node=None,previous_node=None):
        self.data=data
        self.next_node=next_node
        self.previous_node=previous_node

    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data=data

    def get_next(self):
        return self.next_node

    def set_next(self,new_next):
        self.next_node=new_next

    def get_previous(self):
        return self.previous_node

    def set_previous(self,new_node):
        self.previous_node=new_node

class DoublyLinkedList(MyList):
    def __init__ (self,head=None):
        self.head=None
        self.tail=None
        self.length=0

    def len(self):
        return self.length

    def getitem(self,index):
        if(index<0 or index>=self.length):
            raise ValueError ("Index out of range")
        current=self.head
        for i in range (index):
            current=current.get_next
        return current.get_data()

    def setitem(self,data,index):
        if(index<0 or index>=self.length):
            raise ValueError ("Index out of range")
            return
        current=self.head
        for i in range (index):
            current=current.get_next()
        current.set_data(data)

    def insertItem(self,data,index):
        new_node=Node(data)
        if (index==0):
            if (self.head is None):
                self.head=new_node
                self.tail=new_node
            else:
                new_node.next_node=self.head
                self.head.previous_node=new_node
                self.head=new_node

        else:
            current=self.head
            cur_index=0
            while (cur_index<index-1 and current is not None): #cur_index=index-2
                current=current.next_node
                cur_index+=1
            if (current is None):
                raise ValueError ("Index out of range")
            new_node.next_node=current.next_node
            new_node.previous_node=current
            if (current.next_node is not None):
                current.next_node.previous_node=new_node
            else:
                self.tail=new_node
            current.next_node=new_node

    def removeItem(self, index=0):
        if (self.head is None):
            raise ValueError ("List is empty")
        if (index==0):
            if (self.head.next_node is None):
                self.head=None
                self.tail=None
            else: #head노드가 비어있지 않다면
                self.head=self.head.next_node
                self.head.previous_node=None
        else:
            current=self.head
            cur_index=0
            while (cur_index<index and current is not None): #index-2 까지 이동
                current=current.next_node #current는 index까지 이동
                cur_index+=1
            if (current is None):
                raise ValueError ("Index out of range")
            if (current.next_node is None):
                self.tail=current.previous_node
                self.tail.next_node=None
            else:
                current.previous_node.next_node=current.next_node
                current.next_node.previous_node=current.previous_node

    def printMyList(self):
        current = self.head
        while current:
            print(current.get_data(), end=" ")
            current = current.next_node
        print()

my_list=DoublyLinkedList()
my_list.insertItem(4,0)
my_list.insertItem(3,0)
my_list.insertItem(1,0)
my_list.insertItem(2,1)
my_list.printMyList()
my_list.removeItem(3)
my_list.removeItem(1)
my_list.removeItem(0)
my_list.printMyList()
