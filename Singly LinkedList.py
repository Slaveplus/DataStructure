from MyList import MyList
class Node(object):
    def __init__ (self, data=None, next_node=None):
        self.data=data
        self.next_node=next_node

    def get_data(self):
        return self.data

    def set_data(self,data): #데이터를 다시 저장할때 사용
        self.data=data

    def get_next(self):
        return self.next_node

    def set_next(self,new_next): #다음 노드를 변경할 때 사용
        self.next_node=new_next

class SinglyLinkedList(MyList):
    def __init__ (self,head=None):
        self.head=None
        self.length=0

    def len(self):
        return self.length

    def getitem(self,j):
        if(j<0 or j>=self.length):
            raise ValueError ("Index out of range")
        current=self.head #제일 앞에있는 head노드를 선택함
        for i in range(j): #얻어오려는 노드까지 이동하기 위해 for문으로 j번째 노드까지 이동
            current=current.get_next()
        return current.get_data() #j-1번째까지 이동한후 다음 노드의 데이터를 가져옴

    def setitem(self,val,j):
        if(j<0 or j>self.length):
            raise ValueError("Index out of range")
        current=self.head
        for i in range(j):
            current=current.get_next()
        current.set_data(val)

    def insertItem(self, item , j=0):
        new_node=Node(item)
        self.length+=1
        if (j==0):
            if (self.head is None):
                self.head=new_node
            else:
                new_node.next_node=self.head
                self.head=new_node
        else:
            current=self.head
            cur_index=0
            while current.next_node and cur_index<j-1:
                current=current.next_node
                cur_index+=1
            if (cur_index==j-1): #j인덱스의 기존 노드의 연결을 끊고 새로운 노드에 연결시킴
                new_node.next_node=current.next_node
                current.next_node=new_node
            else:
                self.length-=1
                raise ValueError ("Index out of range")


    def removeItem(self,j=0):
        current=self.head
        self.length-=1
        cur_index=0
        if (j==0):
            self.head=current.next_node #처음 노드의 다음 노드로 처음노드를 변경
            return
        while current.next_node and cur_index<j-1:
            current=current.next_node
            cur_index+=1
        if (cur_index==j-1):
            bf_node=current
            cur_index+=1
            current=current.next_node
        if (cur_index==j):
            bf_node.set_next(current.next_node)
            del(current)
        else:
            raise ValueError ("Index out of range")
            self.length+=1


    def printMyList(self):
        current=self.head
        while current:
            print(current.get_data(), end=" " )
            current=current.next_node
        print()

my_list=SinglyLinkedList()
my_list.insertItem(4,0)
my_list.insertItem(3,0)
my_list.insertItem(1,0)
my_list.insertItem(2,1)
my_list.printMyList()
my_list.removeItem(3)
my_list.removeItem(1)
my_list.removeItem(0)
my_list.printMyList()